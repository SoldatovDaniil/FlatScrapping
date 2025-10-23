import sqlalchemy as sa

from app.parsers.cian import CianParser
from app.models.rent import Rent
from app.core.database import session_maker


class ParserService():
    def __init__(self, parser):
        self.parser = parser


    def parse_and_store_ads(self, url=None):
        session = session_maker()

        try:
            ads_list = self.parser.parse_appartments_list(url)
            
            if not ads_list:
                print("Cant get ads")
                return 
            
            new_ads_count = 0

            for ad in ads_list:
                query = sa.select(Rent).where(Rent.external_id == ad['external_id'])
                existing_ad = session.scalar(query)
                if not existing_ad:
                    new_ad = Rent(**ad)
                    session.add(new_ad)
                    new_ads_count += 1 
            session.commit()

            return ads_list

        except Exception as e:
            print(f"Error: {e}")
            session.rollback()
            return 
        
        finally:
            session.close()
    

    def get_last_ad(self):
        session = session_maker()
        try:
            query = sa.select(Rent).order_by(sa.desc(Rent.date))
            ad = session.scalar(query)
            return ad
        
        except Exception as e:
            print(f"Error: {e}")
            session.rollback()
            return 
        
        finally:
            session.close()
    
            

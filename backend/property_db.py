import sqlite3
from property import Property

class PropertyRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def save_properties(self, properties):
        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()

            cursor.execute('CREATE TABLE IF NOT EXISTS properties (financial text, city text, address text, type text, style text, mls_number text, date text, status text, bedrooms integer, bathrooms integer, year_built integer, square_feet integer, acres real, school_district text, company text)')

            for prop in properties:
                cursor.execute('INSERT INTO properties (financial, city, address, type, style, mls_number, date, status, bedrooms, bathrooms, year_built, square_feet, acres, school_district, company) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (prop.financial, prop.city, prop.address, prop.type, prop.style, prop.mls_number, prop.date, prop.status, prop.bedrooms, prop.bathrooms, prop.year_built, prop.square_feet, prop.acres, prop.school_district, prop.company))

            db.commit()
            
    def get_properties_with_pagination(self, page: int, size: int):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT *
                FROM properties
                LIMIT :size
                OFFSET :page * :size
            """, {
                "size": size,
                "page": page,
            })
            
        properties = []
        
        for row in cursor:
            properties.append(Property(financial=row[0], city=row[1], address=row[2], type=row[3], style=row[4], mls_number=row[5], date=row[6], status=row[7], bedrooms=row[8], bathrooms=row[9], year_built=row[10], square_feet=row[11], acres=row[12], school_district=row[13], company=row[14]))
                
        return properties

    def get_properties(self):
        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()

            cursor.execute('SELECT * FROM properties')

            properties = []

            for row in cursor:
                properties.append(Property(financial=row[0], city=row[1], address=row[2], type=row[3], style=row[4], mls_number=row[5], date=row[6], status=row[7], bedrooms=row[8], bathrooms=row[9], year_built=row[10], square_feet=row[11], acres=row[12], school_district=row[13], company=row[14]))
                
            return properties
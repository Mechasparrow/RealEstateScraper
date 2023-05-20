import json

class Property:
    def __init__(self, financial=None, city=None, address=None, type=None, style=None, mls_number=None, date=None, status=None, bedrooms=None, bathrooms=None, year_built=None, square_feet=None, acres=None, school_district=None, company=None):
        self.financial = financial
        self.city = city
        self.address = address
        self.type = type
        self.style = style
        self.mls_number = mls_number
        self.date = date
        self.status = status
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.year_built = year_built
        self.square_feet = square_feet
        self.acres = acres
        self.school_district = school_district
        self.company = company
        
    def __repr__(self):
        return f"Property(financial={self.financial}, city={self.city}, address={self.address}, type={self.type}, style={self.style}, mls_number={self.mls_number}, date={self.date}, status={self.status}, bedrooms={self.bedrooms}, bathrooms={self.bathrooms}, year_built={self.year_built}, square_feet={self.square_feet}, acres={self.acres}, school_district={self.school_district}, company={self.company})"
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    def __dict__(self):
        return {
            "financial": self.financial,
            "city": self.city,
            "address": self.address,
            "type": self.type,
            "style": self.style,
            "mls_number": self.mls_number,
            "date": self.date,
            "status": self.status,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "year_built": self.year_built,
            "square_feet": self.square_feet,
            "acres": self.acres,
            "school_district": self.school_district,
            "company": self.company,
        }
    
    def json_to_property(data):
        prop = Property()
        prop.financial = data.get("financial")
        prop.city = data.get("city")
        prop.address = data.get("address")
        prop.type = data.get("type")
        prop.style = data.get("style")
        prop.mls_number = data.get("mls-number")
        prop.date = data.get("date")
        prop.status = data.get("status")
        prop.bedrooms = data.get("bedrooms")
        prop.bathrooms = data.get("bathrooms")
        prop.year_built = data.get("year_built")
        prop.square_feet = data.get("square_feet")
        prop.acres = data.get("acres")
        prop.school_district = data.get("school_district")
        prop.company = data.get("company")
        
        return prop
    
class PropertyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Property):
            return {
                "financial": obj.financial,
                "city": obj.city,
                "address": obj.address,
                "type": obj.type,
                "style": obj.style,
                "mls_number": obj.mls_number,
                "date": obj.date,
                "status": obj.status,
                "bedrooms": obj.bedrooms,
                "bathrooms": obj.bathrooms,
                "year_built": obj.year_built,
                "square_feet": obj.square_feet,
                "acres": obj.acres,
                "school_district": obj.school_district,
                "company": obj.company,
            }
        else:
            return super().default(obj)
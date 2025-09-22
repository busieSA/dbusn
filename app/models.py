from app.basemodel import db , BaseMixin

class Region(BaseMixin, db.Model):
    __tablename__ = 'regions'

    name = db.Column(db.String(), nullable=False) # Central ,North and South
    descritpion = db.Column(db.Text, nullable=False)

    #relates to Area

    areas = db.relationship(
        'Area',
        backref='region', 
        lazy=True
    )

class Area(BaseMixin, db.Model):
    __tablename__ = 'areas'

    name = db.Column(db.String(), nullable=False)  # eg chesterville, KwaMashu, Durban North and ect...

    # map to This Region
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)

    #relates to Routes

    routes = db.relationship(
        'Route', 
        backref='area',
        lazy=True
    )

class Route(BaseMixin, db.Model):
    __tablename__ = 'routes'

    route_number = db.Column(db.String(), nullable=False) # '60', '716' , etc
    name = db.Column(db.String(), nullable=True) # Descriptive name fort the route
    direction = db.Column(db.String(), nullable=True) # From KwaMashu, To KwaMashu

    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    
    #key to bus service
    bus_service_id = db.Column(db.Integer, db.ForeignKye('bus_services.id'), nullable=False)

    #relates to bus schedules
    schedules = db.relationship(
        'Schedule',
        backref='route', 
        lazy=True
    )

    #Composite
    __table_args__ = (
        db.Index(
            'idx_route_area_service',
            'route_number', 
            'area_id',
            'bus_service_id'
        ),
    )

class Location(BaseMixin, db.Model):
    __tablename__ = ' locations'

    name = db.Column(db.String(), nullable=False) # City, Point , Marin Garage and ect
    type_stop = db.Column(db.String(), nullable=True) # 'Terminal', "Stop", "land Mark" ect
    
    #Relates to To a& From 
    from_schedules = db.realtionship(
        "Schedule", 
        foreign_kkey="Schedule.from_location_id",
        backref="from_location"
    )

    to_schedules = db.relationship(
        "Schedule",
        foreign_keys = "Schedule.to_location_id",
        backref="to_location"
    )

class Schedule(BaseMixin, db.Model):
    __tablename__ = 'schedules'
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'), nullable=False)

    #to & From id mapping
    # 
    from_location_id = db.Column(db.Integer, db.ForiegnKey('locations.id'), nullable=False)
    to_location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)

    departure_time = db.Column(db.Time, nullable=False)
    day_type = db.Column(db.String(), nullable=False) # "weekday", saturday, sunday 

    notes = db.Column(db.text, nullable=True)

    #composite for queries
    __table_args__ = (
        db.Index(
            'idx_schedule_route_day', 
            'route_id', 
            'day_type'
        ),
        db.Index(
            'idx_schedule_time_day', 
            'pedarture_time', 
            'day_type'
        ),
    )






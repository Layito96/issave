# -*- coding: utf-8 -*-

from gluon import current
from s3 import *
from s3layouts import *
try:
    from .layouts import *
except ImportError:
    pass
import s3menus as default

# =============================================================================
class S3MainMenu(default.S3MainMenu):
    """ Custom Application Main Menu """

    # -------------------------------------------------------------------------
    @classmethod
    def menu_modules(cls):
        """ Custom Modules Menu """

        menu= [MM("Call Logs", c="event", f="incident_report", m="summary"),
               MM("Incidents", c="event", f="incident", m="summary"),
               MM("Scenarios", c="event", f="scenario"),
               MM("more", c="event", f="more")(
                MM("Events", c="event", f="event"),
                MM("Staff", c="hrm", f="staff"),
                MM("Volunteers", c="vol", f="volunteer"),
                # MM("Assets", c="asset", f="asset"),
                MM("Articles", c="asset", f="item", m="summary"),
                MM("Organizations", c="org", f="organisation"),
                MM("Facilities", c="org", f="facility"),
                MM("Hospitals", c="hms", f="hospital", m="summary"),
                # MM("Shelters", c="cr", f="shelter"),
                MM("Warehouses", c="inv", f="warehouse"),
                # MM("Item Catalog", c="supply", f="catalog_item"),
                MM("Map", c="gis", f="index"),
                ),
               ]

        return menu


# =============================================================================
class S3OptionsMenu(default.S3OptionsMenu):
    """ Custom Controller Menus """

    # -------------------------------------------------------------------------
    def event(self):
        """ Events menu """

        if current.deployment_settings.get_event_label(): # == "Disaster"
            EVENTS = "Disasters"
            EVENT_TYPES = "Disaster Types"
        else:
            EVENTS = "Events"
            EVENT_TYPES = "Event Types"

        return M()(
		           M("Sous-menu", link=False)(
                       # M("Scenarios", c="event", f="scenario")(
                           # M("Create", m="create"),
                       # ),
                       # M(EVENTS, c="event", f="event")(
                           # M("Create", m="create"),
                       # ),
                       M(EVENT_TYPES, c="event", f="event_type")(
                           # M("Create", m="create"),
                       ),
                       # M("Incidents", c="event", f="incident")(
                           # M("Create", m="create"),
                       # ),
                       # M("Incident Reports", c="event", f="incident_report", m="summary")(
                           # M("Create", m="create"),
                       # ),
                       M("Incident Types", c="event", f="incident_type")(
                           # M("Create", m="create"),
                       ),
                       M("Positions", c="event", f="job_title")(
                           # M("Create", m="create"),
                       ),
                       M("Situation Reports", c="event", f="sitrep")(
                           # M("Create", m="create"),
                       ),
                    )
                )

    # -------------------------------------------------------------------------
    def scenario(self):
        """ Scenario menu """

        return self.event()

# END =========================================================================

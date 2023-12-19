# -*- coding: utf-8 -*-

from gluon import *
from s3 import S3CustomController

THEME = "SAFIRE"

# =============================================================================


class index(S3CustomController):
    """ Custom Home Page """

    def __call__(self):

        # redirect(URL(c="event", f="incident_report", args = "summary"))
        output = {}

        # Allow editing of page content from browser using CMS module
        if current.deployment_settings.has_module("cms"):
            system_roles = current.auth.get_system_roles()
            ADMIN = system_roles.ADMIN in current.session.s3.roles
            s3db = current.s3db
            table = s3db.cms_post
            ltable = s3db.cms_post_module
            module = "default"
            resource = "index"
            query = (ltable.module == module) & \
                    ((ltable.resource == None) |
                     (ltable.resource == resource)) & \
                    (ltable.post_id == table.id) & \
                    (table.deleted != True)
            item = current.db(query).select(table.body,
                                            table.id,
                                            limitby=(0, 1)).first()
            if item:
                if ADMIN:
                    item = DIV(XML(item.body),
                               BR(),
                               A(current.T("Edit"),
                                 _href=URL(c="cms", f="post",
                                           args=[item.id, "update"]),
                                 _class="btn btn-primary"))
                else:
                    item = DIV(XML(item.body))
            elif ADMIN:
                if current.response.s3.crud.formstyle == "bootstrap":
                    _class = "btn"
                else:
                    _class = "btn btn-primary"
                item = A(current.T("Edit"),
                         _href=URL(c="cms", f="post", args="create",
                                   vars={"module": module,
                                         "resource": resource
                                         }),
                         _class="%s cms-edit" % _class)
            else:
                item = ""
        else:
            from s3layouts import S3HomepageMenuLayout as HM

            sit_menu = HM("Conscience de la situation")(
                HM("Map", c="gis", f="index", icon="map-marker"),
                HM("Incidents", c="event", f="incident_report", icon="incident"),
                HM("Alerts", c="cap", f="alert", icon="alert"),
                HM("Assessments", c="survey", f="series", icon="assessment"),
            )
            org_menu = HM("Qui fait quoi et où")(
                HM("Organizations", c="org", f="organisation", icon="organisation"),
                HM("Facilities", c="org", f="facility", icon="facility"),
                # HM("Activities", c="project", f="activity", icon="activity"),
                # HM("Projects", c="project", f="project", icon="project"),
            )
            res_menu = HM("Gérer les ressources")(
                HM("Staff", c="hrm", f="staff",
                   t="hrm_human_resource", icon="staff"),
                HM("Volunteers", c="vol", f="volunteer",
                   t="hrm_human_resource", icon="volunteer"),
                HM("Relief Goods", c="inv", f="inv_item", icon="goods"),
                HM("Assets", c="asset", f="asset", icon="asset"),
            )
            aid_menu = HM("Gérer l'aide")(
                HM("Requests", c="req", f="req", icon="request"),
                HM("Commitments", c="req", f="commit", icon="commit"),
                HM("Sent Shipments", c="inv", f="send", icon="shipment"),
                HM("Received Shipments", c="inv", f="recv", icon="delivery"),
            )
            item = ""
        # output["item"] = item
        output = {"title": "",

                  # CMS Contents
                  "item": item,

                  # Menus
                  "sit_menu": sit_menu,
                  "org_menu": org_menu,
                  "res_menu": res_menu,
                  "aid_menu": aid_menu,
                  # "facility_box": facility_box,

                  # Quick Access Boxes
                  # "manage_facility_box": manage_facility_box,
                  # "org_box": org_box,

                  # Login Form
                  # "login_div": login_div,
                  # "login_form": login_form,

                  # Registration Form
                  # "register_div": register_div,
                  # "register_form": register_form,

                  # Control Data
                  # "self_registration": self_registration,
                  # "registered": registered,
                  # "r": None, # Required for dataTable to work
                  # "datatable_ajax_source": datatable_ajax_source,

                  }
        self._view(THEME, "index.html")
        return output

# END =========================================================================

# -*- coding: utf-8 -*-

from gluon import current

def config(settings):
    """
        Template settings for Sweden
        - designed to be used in a Cascade with an application template
    """

    #T = current.T

    # Pre-Populate
    settings.base.prepopulate.append("locations/SE")

    # Uncomment to restrict to specific country/countries
    settings.gis.countries.append("SE")
    # Disable the Postcode selector in the LocationSelector
    #settings.gis.postcode_selector = False

    # L10n (Localization) settings
    settings.L10n.languages["sv"] = "Swedish"
    # Default Language (put this in custom template if-required)
    #settings.L10n.default_language = "sv"
    # Default timezone for users
    settings.L10n.timezone = "Europe/Stockholm"
    # Default Country Code for telephone numbers
    settings.L10n.default_country_code = 46

    settings.fin.currencies["SEK"] = "Swedish Krona"
    settings.fin.currency_default = "SEK"

# END =========================================================================

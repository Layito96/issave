<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

    <!-- **********************************************************************
         Staff Levels - CSV Import Stylesheet

         CSV fields:
         Name............................hrm_staff_level.name
         Organisation....................hrm_staff_level.organisation

    *********************************************************************** -->
    <xsl:import href="../commons.xsl"/>
    <xsl:import href="salary.xsl"/>

    <xsl:output method="xml"/>

    <xsl:key name="organisation" match="row" use="col[@field='Organisation']"/>

    <!-- ****************************************************************** -->
    <xsl:template match="/">
        <s3xml>
            <!-- Organisations -->
            <xsl:for-each select="//row[generate-id(.)=generate-id(key('organisation', col[@field='Organisation'])[1])]">
                <xsl:call-template name="Organisation"/>
            </xsl:for-each>

            <xsl:apply-templates select="table/row"/>
        </s3xml>
    </xsl:template>

    <!-- ****************************************************************** -->
    <xsl:template match="row">
        <xsl:call-template name="StaffLevel"/>
    </xsl:template>

    <!-- ****************************************************************** -->

</xsl:stylesheet>

# Generated by Django 2.2.13 on 2020-09-28 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0040_auto_20200717_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='fqdn',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='endpoint',
            name='port',
            field=models.IntegerField(blank=True, help_text='The network port associated with the endpoint.', null=True),
        ),
        migrations.AddField(
            model_name='finding',
            name='sourcefile',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='finding',
            name='sourcefilepath',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='child_rule',
            name='match_field',
            field=models.CharField(choices=[('id', 'id'), ('title', 'title'), ('date', 'date'), ('cwe', 'cwe'), ('cve', 'cve'), ('url', 'url'), ('severity', 'severity'), ('description', 'description'), ('mitigation', 'mitigation'), ('impact', 'impact'), ('steps_to_reproduce', 'steps_to_reproduce'), ('severity_justification', 'severity_justification'), ('references', 'references'), ('test', 'test'), ('is_template', 'is_template'), ('active', 'active'), ('verified', 'verified'), ('false_p', 'false_p'), ('duplicate', 'duplicate'), ('duplicate_finding', 'duplicate_finding'), ('out_of_scope', 'out_of_scope'), ('under_review', 'under_review'), ('review_requested_by', 'review_requested_by'), ('under_defect_review', 'under_defect_review'), ('defect_review_requested_by', 'defect_review_requested_by'), ('is_Mitigated', 'is_Mitigated'), ('thread_id', 'thread_id'), ('mitigated', 'mitigated'), ('mitigated_by', 'mitigated_by'), ('reporter', 'reporter'), ('numerical_severity', 'numerical_severity'), ('last_reviewed', 'last_reviewed'), ('last_reviewed_by', 'last_reviewed_by'), ('line_number', 'line_number'), ('sourcefilepath', 'sourcefilepath'), ('sourcefile', 'sourcefile'), ('param', 'param'), ('payload', 'payload'), ('hash_code', 'hash_code'), ('line', 'line'), ('file_path', 'file_path'), ('component_name', 'component_name'), ('component_version', 'component_version'), ('static_finding', 'static_finding'), ('dynamic_finding', 'dynamic_finding'), ('created', 'created'), ('jira_creation', 'jira_creation'), ('jira_change', 'jira_change'), ('scanner_confidence', 'scanner_confidence'), ('sonarqube_issue', 'sonarqube_issue'), ('unique_id_from_tool', 'unique_id_from_tool'), ('sast_source_object', 'sast_source_object'), ('sast_sink_object', 'sast_sink_object'), ('sast_source_line', 'sast_source_line'), ('sast_source_file_path', 'sast_source_file_path'), ('nb_occurences', 'nb_occurences')], max_length=200),
        ),
        migrations.AlterField(
            model_name='rule',
            name='applied_field',
            field=models.CharField(choices=[('id', 'id'), ('title', 'title'), ('date', 'date'), ('cwe', 'cwe'), ('cve', 'cve'), ('url', 'url'), ('severity', 'severity'), ('description', 'description'), ('mitigation', 'mitigation'), ('impact', 'impact'), ('steps_to_reproduce', 'steps_to_reproduce'), ('severity_justification', 'severity_justification'), ('references', 'references'), ('test', 'test'), ('is_template', 'is_template'), ('active', 'active'), ('verified', 'verified'), ('false_p', 'false_p'), ('duplicate', 'duplicate'), ('duplicate_finding', 'duplicate_finding'), ('out_of_scope', 'out_of_scope'), ('under_review', 'under_review'), ('review_requested_by', 'review_requested_by'), ('under_defect_review', 'under_defect_review'), ('defect_review_requested_by', 'defect_review_requested_by'), ('is_Mitigated', 'is_Mitigated'), ('thread_id', 'thread_id'), ('mitigated', 'mitigated'), ('mitigated_by', 'mitigated_by'), ('reporter', 'reporter'), ('numerical_severity', 'numerical_severity'), ('last_reviewed', 'last_reviewed'), ('last_reviewed_by', 'last_reviewed_by'), ('line_number', 'line_number'), ('sourcefilepath', 'sourcefilepath'), ('sourcefile', 'sourcefile'), ('param', 'param'), ('payload', 'payload'), ('hash_code', 'hash_code'), ('line', 'line'), ('file_path', 'file_path'), ('component_name', 'component_name'), ('component_version', 'component_version'), ('static_finding', 'static_finding'), ('dynamic_finding', 'dynamic_finding'), ('created', 'created'), ('jira_creation', 'jira_creation'), ('jira_change', 'jira_change'), ('scanner_confidence', 'scanner_confidence'), ('sonarqube_issue', 'sonarqube_issue'), ('unique_id_from_tool', 'unique_id_from_tool'), ('sast_source_object', 'sast_source_object'), ('sast_sink_object', 'sast_sink_object'), ('sast_source_line', 'sast_source_line'), ('sast_source_file_path', 'sast_source_file_path'), ('nb_occurences', 'nb_occurences')], max_length=200),
        ),
        migrations.AlterField(
            model_name='rule',
            name='match_field',
            field=models.CharField(choices=[('id', 'id'), ('title', 'title'), ('date', 'date'), ('cwe', 'cwe'), ('cve', 'cve'), ('url', 'url'), ('severity', 'severity'), ('description', 'description'), ('mitigation', 'mitigation'), ('impact', 'impact'), ('steps_to_reproduce', 'steps_to_reproduce'), ('severity_justification', 'severity_justification'), ('references', 'references'), ('test', 'test'), ('is_template', 'is_template'), ('active', 'active'), ('verified', 'verified'), ('false_p', 'false_p'), ('duplicate', 'duplicate'), ('duplicate_finding', 'duplicate_finding'), ('out_of_scope', 'out_of_scope'), ('under_review', 'under_review'), ('review_requested_by', 'review_requested_by'), ('under_defect_review', 'under_defect_review'), ('defect_review_requested_by', 'defect_review_requested_by'), ('is_Mitigated', 'is_Mitigated'), ('thread_id', 'thread_id'), ('mitigated', 'mitigated'), ('mitigated_by', 'mitigated_by'), ('reporter', 'reporter'), ('numerical_severity', 'numerical_severity'), ('last_reviewed', 'last_reviewed'), ('last_reviewed_by', 'last_reviewed_by'), ('line_number', 'line_number'), ('sourcefilepath', 'sourcefilepath'), ('sourcefile', 'sourcefile'), ('param', 'param'), ('payload', 'payload'), ('hash_code', 'hash_code'), ('line', 'line'), ('file_path', 'file_path'), ('component_name', 'component_name'), ('component_version', 'component_version'), ('static_finding', 'static_finding'), ('dynamic_finding', 'dynamic_finding'), ('created', 'created'), ('jira_creation', 'jira_creation'), ('jira_change', 'jira_change'), ('scanner_confidence', 'scanner_confidence'), ('sonarqube_issue', 'sonarqube_issue'), ('unique_id_from_tool', 'unique_id_from_tool'), ('sast_source_object', 'sast_source_object'), ('sast_sink_object', 'sast_sink_object'), ('sast_source_line', 'sast_source_line'), ('sast_source_file_path', 'sast_source_file_path'), ('nb_occurences', 'nb_occurences')], max_length=200),
        ),
    ]

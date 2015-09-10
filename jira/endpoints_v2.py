"""
API MAPPING FOR JIRA API V2
"""

mapping_table = {

    'content_type': 'application/json',
    'path_prefix': '/rest/api/2',

    # Custom field options
    'get_custom_field_option': {
        'path': '/customFieldOption/{{custom_field_option}}'
    },


    # Fields
    'list_fields': {
        'path': '/field'
    },

    # Issues
    'get_issue': {
        'path': '/issue/{{issue}}'
    },
    'create_issue': {
        'method': 'POST',
        'path': '/issue',
        'status': 201
    },
    'update_issue': {
        'method': 'PUT',
        'path': '/issue/{{issue}}',
        'status': 204
    },
    'delete_issue': {
        'method': 'DELETE',
        'path': '/issue/{{issue}}',
        'status': 204
    },
    'assign_issue': {
        'method': 'PUT',
        'path': '/issue/{{issue}}/assignee',
        'status': 204
    },
    'search_issues': {
        'path': '/search',
        'valid_params': ['jql','startAt','maxResults']
    },

    # Issue attachments
    'add_attachment': {
        'method': 'POST',
        'path': '/issue/{{issue}}/attachments',
        'content_type': 'multipart/form-data'
    },

    # Issue comments
    'list_comments': {
        'path': '/issue/{{issue}}/comment',
        'valid_params': ['startAt','maxResults']
    },
    'add_comment': {
        'method': 'POST',
        'path': '/issue/{{issue}}/comment',
        'status': 201
    },
    'get_comment': {
        'path': '/issue/{{issue}}/comment/{{comment}}'
    },
    'update_comment': {
        'method': 'PUT',
        'path': '/issue/{{issue}}/comment/{{comment}}'
    },
    'delete_comment': {
        'method': 'DELETE',
        'path': '/issue/{{issue}}/comment/{{comment}}',
        'status': 204
    },

    # Issue create metadata
    'get_create_metadata':  {
        'path': '/issue/createmeta'
    },

    # Issue edit metadata
    'get_edit_metadata':  {
        'path': '/issue/{{issue}}/editmeta'
    },

    # Issue link types
    'list_issue_link_types': {
        'path': '/issueLinkType'
    },

    # Issue links
    'get_issue_link': {
        'path': '/issueLink/{{link}}'
    },
    'create_issue_link': {
        'method': 'POST',
        'path': '/issueLink',
        'status': 201
    },
    'delete_issue_link': {
        'method': 'DELETE',
        'path': '/issueLink/{{link}}',
        'status': 204
    },

    # Issue remote links
    'list_issue_remote_links': {
        'path': '/issue/{{issue}}/remotelink'
    },
    'add_issue_remote_link': {
        'method': 'POST',
        'path': '/issue/{{issue}}/remotelink',
        'status': 201
    },
    'get_issue_remote_link': {
        'path': '/issue/{{issue}}/remotelink/{{link}}'
    },
    'update_issue_remote_link': {
        'method': 'PUT',
        'path': '/issue/{{issue}}/remotelink/{{link}}',
        'status': 204
    },
    'delete_issue_remote_link': {
        'method': 'DELETE',
        'path': '/issue/{{issue}}/remotelink/{{link}}',
        'status': 204
    },

    # Issue transitions
    'list_issue_transitions': {
        'path': '/issue/{{issue}}/transitions'
    },
    'transition_issue': {
        'method': 'POST',
        'path': '/issue/{{issue}}/transitions',
        'status': 204
    },

    # Issue types
    'list_issue_types': {
        'path': '/issuetype'
    },

    # Issue votes
    'list_votes': {
        'path': '/issue/{{issue}}/votes'
    },
    'add_vote': {
        'method': 'POST',
        'path': '/issue/{{issue}}/votes',
        'status': 204
    },
    'delete_vote': {
        'method': 'DELETE',
        'path': '/issue/{{issue}}/votes',
        'status': 204
    },

    # Issue watchers
    'list_watchers': {
        'path': '/issue/{{issue}}/watchers'
    },
    'add_watcher': {
        'method': 'POST',
        'path': '/issue/{{issue}}/watchers',
        'status': 204
    },
    'delete_watcher': {
        'method': 'DELETE',
        'path': '/issue/{{issue}}/watchers',
        'valid_params': ['username'],
        'status': 204
    },

    # Projects
    'get_project': {
        'path': '/project/{{project}}'
    },
    'list_projects': {
        'path': '/project'
    },

    # Project components
    'list_project_components': {
        'path': '/project/{{project}}/components'
    },

    # Project statuses
    'list_project_statuses': {
        'path': '/project/{{project}}/statuses'
    },

    # Project versions
    'list_project_versions': {
        'path': '/project/{{project}}/versions',
        'valid_params': ['startAt','maxResults']
    },

    # Resolutions
    'get_resolution': {
        'path': '/resolution/{{resolution}}'
    },
    'list_resolutions': {
        'path': '/resolution'
    },

    # Statuses
    'get_status': {
        'path': '/status/{{status}}'
    },
    'list_statuses': {
        'path': '/status'
    },

}

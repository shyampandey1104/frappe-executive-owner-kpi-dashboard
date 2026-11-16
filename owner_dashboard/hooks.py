# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "owner_dashboard"
app_title = "Frappe Executive Owner Kpi Dashboard"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Executive Owner Kpi Dashboard for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/owner_dashboard/css/owner_dashboard.bundle.css"
app_include_js = "/assets/owner_dashboard/js/owner_dashboard.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "owner_dashboard.engine.on_document_submit",
        "on_cancel": "owner_dashboard.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "owner_dashboard.engine.daily_scheduled_sync"
    ]
}

from flask_admin.contrib.sqla import ModelView


class UserModelView(ModelView):
    # Fields to display in the list view
    form_columns = ['id', 'username', 'email', 'plan', 'billing', 'subscription_start_date', 'subscription_end_date']
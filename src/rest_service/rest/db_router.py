router_dict_based_on_app_name = {
    "team": "evaluation",
    "test": "evaluation",
}

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """
        reads from evaluation if not django model
        """
        return router_dict_based_on_app_name.get(model._meta.app_label, "default")

    def db_for_write(self, model, **hints):
        return router_dict_based_on_app_name.get(model._meta.app_label, "default")

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db == obj2._state.db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return router_dict_based_on_app_name.get(app_label, "default") == db

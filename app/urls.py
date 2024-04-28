from django.urls import path
from app.views import sign_up, dashboard
urlpatterns = [
    # URLs related to home page
    path("", sign_up.login_page, name="login_page"),
    path("login", sign_up.login_page, name="login"),
    path("user_login", sign_up.user_login, name="user_login"),
    path("user_logout", sign_up.user_logout, name="user_logout"),
    path("register", sign_up.register, name="register"),
    path("register_new_user", sign_up.register_new_user, name="register_new_user"),
    path("dashboard", dashboard.dashboard, name="dashboard"),
    path("user_list", dashboard.user_list, name="user_list"),
    path("product_list", dashboard.product_list, name="product_list"),
    path("add_product", dashboard.add_product, name="add_product"),
    path("add_product_in_assembly", dashboard.add_product_in_assembly, name="add_product_in_assembly"),
    path("update_product_in_assembly/<int:id>", dashboard.update_product_in_assembly, name="update_product_in_assembly"),
    path("repair_product", dashboard.repaired_product_list, name="repair_product"),
    path("rejected_product", dashboard.rejected_product_list, name="rejected_product"),
    path("product_tracking", dashboard.product_tracking, name="product_tracking"),
    path("analytics_daily_production", dashboard.analytics_daily_production, name="analytics_daily_production"),
    path("analytics_monthly_production", dashboard.analytics_monthly_production, name="analytics_monthly_production"),
    path("analytics_daily_packing", dashboard.analytics_daily_packing, name="analytics_daily_packing"),
    path("analytics_monthly_packing", dashboard.analytics_monthly_packing, name="analytics_monthly_packing"),
    path("analytics_daily_dispatch", dashboard.analytics_daily_dispatch, name="analytics_daily_dispatch"),
    path("analytics_monthly_dispatch", dashboard.analytics_monthly_dispatch, name="analytics_monthly_dispatch"),
    path("analytics_daily_reject", dashboard.analytics_daily_reject, name="analytics_daily_reject"),
    path("analytics_monthly_reject", dashboard.analytics_monthly_reject, name="analytics_monthly_reject"),
]
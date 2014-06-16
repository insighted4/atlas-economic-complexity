#from django.conf.urls import patterns, include, url
#from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
#from django.views.generic.simple import redirect_to
from django.conf.urls import patterns, include
from django.views.generic import TemplateView, RedirectView

# sitemap
from django.conf.urls.defaults import *
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf import settings


sitemaps = {
    'flatpages': FlatPageSitemap,
}


if not settings.HTTP_HOST:
  HTTP_HOST = '/'
else:
  HTTP_HOST = settings.HTTP_HOST

class TextPlainView(TemplateView):
  def render_to_response(self, context, **kwargs):
    return super(TextPlainView, self).render_to_response(
      context, content_type='text/plain', **kwargs)


urlpatterns = patterns('',

  ## Exploring new patterns
  #(r'^redesign/', include('redesign.urls')),
#  (r'^usa/', include('usa.urls')),
#  (r'^redesign/', include('redesign.urls')),
  ####
  ## Revisiting old patterns
  ####

  # internationalization ######################################################
  (r'^i18n/', include('django.conf.urls.i18n')),
  (r'^set_language/(?P<lang>[a-z-]{2,5})/$', 'observatory.views.set_language'),

  # product classification ####################################################
  (r'^set_product_classification/(?P<prod_class>[a-z0-9]{3,5})/$', 'observatory.views.set_product_classification'),

  # general site ############################################################
  (r'^$', 'observatory.views.home'),
  (r'^download/$', 'observatory.views.download'),

  # about section ###########################################################
  (r'^about/$', 'observatory.views.about'),
  (r'^about/data/$', RedirectView.as_view(url='/about/data/sitc4/')),
  (r'^about/data/(?P<data_type>\w+)/$', "observatory.views.about_data"),
  (r'^about/permissions/$', "observatory.views.permissions"),
  (r'^about/support/$', "observatory.views.support"),
  (r'^about/research/$', "observatory.views.research"),
  (r'^about/glossary/$', "observatory.views.glossary"),
  (r'^about/team/$', "observatory.views.team"),
  (r'^about/data/$', "observatory.views.data"),
  (r'^about/permissions/$', "observatory.views.permissions"),
  (r'^about/privacy/$', "observatory.views.privacy"),
  # blog
  (r'^about/blog/$', "blog.views.blog_index"),
  url(r'^about/blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', "blog.views.blog_post_detail", name="blog_post"),

  # book ###################################################################
  (r'^book/$', 'observatory.views.book'),

  # API #######################################################################
  (r'^api/$', 'observatory.views.api'),
  (r'^api/apps/$', 'observatory.views.api_apps'),
  (r'^api/data/$', 'observatory.views.api_data'),
  (r'^api/views/$', 'observatory.views.api_views'),

  # Story #####
  (r'^generate_png/$', 'observatory.views_stories.generate_png'),
  (r'^mystories/$', 'observatory.views_stories.minestory'),
  (r'^featured/$', 'observatory.views_stories.featurestory'),
  (r'^popular/$', 'observatory.views_stories.popularstory'),
  (r'^published/$', 'observatory.views_stories.publishstory'),
  (r'^endbrowse/$', 'observatory.views_stories.endbrowse'),
  (r'^deleteStory/$', 'observatory.views_stories.deleteStory'),
  (r'^logout/$', 'observatory.views_stories.logout'),
  (r'^updateEditForm/$', 'observatory.views_stories.updateEditForm'),
  (r'^stories/view/(?P<browseStoryId>[a-z0-9A-Z=_]+)/$', 'observatory.views_stories.viewStory'),
  (r'^stories/edit/(?P<editStoryId>[a-z0-9A-Z=_]+)/$', 'observatory.views_stories.editStoryForm'),
  (r'^cancelstory/$', 'observatory.views_stories.cancelstory'),
  (r'^endSaveStory/$', 'observatory.views_stories.endSaveStory'),
  (r'^publishstory/$', 'observatory.views_stories.published'),
  (r'^likeCount/$', 'observatory.views_stories.likeCount'),
  (r'^featurestory/$', 'observatory.views_stories.featured'),
  (r'^endbrowsestory/$', 'observatory.views_stories.endbrowsestory'),
  (r'^browsestories/(?P<browseStoryId>\d+)/$', 'observatory.views_stories.browsestories'),
  (r'^stories/$', 'observatory.views_stories.browseStoryForm'),
  (r'^endSaveStory/$', 'observatory.views_stories.endSaveStory'),
  (r'^browseStoryNext/$', 'observatory.views_stories.browseStoryNext'),
  (r'^browseStoryPrev/$', 'observatory.views_stories.browseStoryPrev'),
  (r'^createStory/$', 'observatory.views_stories.createStory'),

  # Explore (App) #############################################################
  # Legacy app redirect
  (r'^app/(?P<app_name>[a-z0-9_]+)/(?P<trade_flow>\w{6,10})/(?P<filter>[a-z0-9\.]+)/(?P<year>[0-9\.]+)/$', 'observatory.views.app_redirect'),

  # New app URL structure
  (r'^explore/$', 'observatory.views.explore_random'),
  (r'^explore/(?P<app_name>[a-z_]+)/(?P<trade_flow>\w{6,10})/(?P<country1>\w{3,4})/(?P<country2>\w{3,4})/(?P<product>\w{3,4})/(?P<year>[0-9\.]+)/$', 'observatory.views.explore'),
  (r'^explore/(?P<app_name>[a-z_]+)/(?P<trade_flow>\w{6,10})/(?P<country1>\w{3,4})/(?P<country2>\w{3,4})/(?P<product>\w{3,4})/$', 'observatory.views.explore'),

  # Embed URL
  (r'^embed/(?P<app_name>[a-z_]+)/(?P<trade_flow>\w{6,10})/(?P<country1>\w{3,4})/(?P<country2>\w{3,4})/(?P<product>\w{3,4})/(?P<year>[0-9\.]+)/$', 'observatory.views.embed'),

  # API #######################################################################
  (r'^api/(?P<trade_flow>[a-z_]{6,10})/(?P<country1>\w{3})/all/show/(?P<year>[0-9\.]+)/$', 'observatory.views.api_casy'),
  (r'^api/attr_products/(?P<prod_class>hs4)/$', 'observatory.views.attr_products'),
  (r'^api/(?P<trade_flow>[a-z_]{6,10})/(?P<country1>\w{3})/show/all/(?P<year>[0-9\.]+)/$', 'observatory.views.api_csay'),
  (r'^api/(?P<trade_flow>[a-z_]{6,10})/(?P<country1>\w{3})/(?P<country2>\w{3})/show/(?P<year>[0-9\.]+)/$', 'observatory.views.api_ccsy'),
  (r'^api/(?P<trade_flow>[a-z_]{6,10})/(?P<country1>\w{3})/show/(?P<product>\w{4})/(?P<year>[0-9\.]+)/$', 'observatory.views.api_cspy'),
  (r'^api/(?P<trade_flow>[a-z_]{6,10})/show/all/(?P<product>\w{4})/(?P<year>[0-9\.]+)/$', 'observatory.views.api_sapy'),

  (r'^api/near/(?P<country>\w{3})/(?P<year>[0-9\.]+)/(?P<num_prods>\d+)/$', 'observatory.views_exhibit.api_near'),

  (r'^api/search/$', 'observatory.views.api_search'),
  (r'^search/$', 'observatory.views.search'),

  # Overview (Countries) ######################################################
  (r'^country/(?P<country>\w{2,3})/$', 'observatory.views_overview.country2'),
  (r'^hs4/(?P<product>\d{4})/$', 'observatory.views_overview.product'),
  (r'^sitc4/(?P<product>\d{4})/$', 'observatory.views_overview.product'),
  # (r'^profile/(?P<country>\w{2,3})/(?P<trade_flow>[a-z_]{6})/$', 'observatory.views_overview.country'),

  # Overview (Products) ######################################################
  (r'^overview/(?P<product>\d{4})/$', 'observatory.views_overview.product'),
  (r'^overview/(?P<product>\d{4})/(?P<trade_flow>[a-z_]{6})/$', 'observatory.views_overview.product'),

  # Rankings ##################################################################
  (r'^rankings/$', 'observatory.views_rankings.index'),
  (r'^rankings/(?P<category>\w{7})/$', 'observatory.views_rankings.index'),
  (r'^rankings/(?P<category>\w{7})/(?P<year>[0-9\.]+)/$', 'observatory.views_rankings.index'),
  (r'^rankings/(?P<category>\w{7})/download/$', 'observatory.views_rankings.download'),
  (r'^rankings/(?P<category>\w{7})/(?P<year>[0-9\.]+)/download/$', 'observatory.views_rankings.download'),

  # ROBOTS.TXT AND FAVICO ########################################
  url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
  url(r'^favicon\.ico$', RedirectView.as_view(url='/media/img/favicon.ico')),

  url(r'^sitemap\.xml$', RedirectView.as_view(url='/media/sitemaps/sitemap_index.xml')),

)

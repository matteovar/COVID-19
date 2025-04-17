from .Geographic_Analysis import show_geo
from .Vision_on_Pandemic import show_pandemic
from .Comparisons_between_Regions import show_cbr
from .Mortality_and_Recovery import show_mor_rec

pages = {
    "Pandemic Overview": show_pandemic,
    "Geographic Analysis": show_geo,
    "Comparisons between Regions":show_cbr
    "Mortality and Recovery Rates":show_mor_rec
}

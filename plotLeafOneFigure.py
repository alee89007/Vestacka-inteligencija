import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

data="leaf.csv"
names=['class', 'specimen-number', 'eccentricity', 'aspect-ratio', 'elongation', 'solidity', 'stochastic-convexity', 'isoperimetric-factor', 'maximal-indentation-depth', 'lobedness', 'average-intensity', 'average-contrast', 'smoothness', 'third-moment', 'uniformity', 'entropy']
dataset=pd.read_csv(data, names=names)

array=dataset.values

classQuercus_suberX=array[0:12, 0:15]
classQuercus_suberY=array[0:12, 0]

classSalix_atrocineraX=array[12:22, 0:15]
classSalix_atrocineraY=array[12:22, 0]

classPopulus_nigraX=array[22:32, 0:15]
classPopulus_nigraY=array[22:32, 0]

classAlnus_spX=array[32:40, 0:15]
classAlnus_spY=array[32:40, 0]

classQuercus_roburX=array[40:52, 0:15]
classQuercus_roburY=array[40:52, 0]

classCrataegus_monogynaX=array[52:60, 0:15]
classCrataegus_monogynaY=array[52:60, 0]

classIlex_aquifolimX=array[60:70, 0:15]
classIlex_aquifolimY=array[60:70, 0]

classNerium_oleanderX=array[70:81, 0:15]
classNerium_oleanderY=array[70:81, 0]

classBetula_pubescensX=array[81:95, 0:15]
classBetula_pubescensY=array[81:95, 0]

classTilia_tomentosaX=array[95:108, 0:15]
classTilia_tomentosaY=array[95:108, 0]

classAcer_palmatumX=array[108:124, 0:15]
classAcer_palmatumY=array[108:124, 0]

classCeltis_spX=array[124:136, 0:15]
classCeltis_spY=array[124:136, 0]

classCorylus_avellanaX=array[136:149, 0:15]
classCorylus_avellanaY=array[136:149, 0]

classCastanea_sativaX=array[149:161, 0:15]
classCastanea_sativaY=array[149:161, 0]

classPopulus_albaX=array[161:171, 0:15]
classPopulus_albaY=array[161:171, 0]

classPrimula_vulgarisX=array[171:183, 0:15]
classPrimula_vulgarisY=array[171:183, 0]

classErodium_spX=array[183:194, 0:15]
classErodium_spY=array[183:194, 0]

classBougainvillea_spX=array[194:207, 0:15]
classBougainvillea_spY=array[194:207, 0]

classArisarum_vulgareX=array[207:216, 0:15]
classArisarum_vulgareY=array[207:216, 0]

classEnonymus_japonicusX=array[216:228, 0:15]
classEnonymus_japonicusY=array[216:228, 0]

classIlex_perado_ssp_azoricaX=array[228:239, 0:15]
classIlex_perado_ssp_azoricaY=array[228:239, 0]

classMagnolia_soulangeanaX=array[239:251, 0:15]
classMagnolia_soulangeanaY=array[239:251, 0]

classBuxus_sempervirensX=array[251:263, 0:15]
classBuxus_sempervirensY=array[251:263, 0]

classUrtica_dioicaX=array[263:275, 0:15]
classUrtica_dioicaY=array[263:275, 0]

classPodocarpus_spX=array[275:286, 0:15]
classPodocarpus_spY=array[275:286, 0]

classAcca_sellowianaX=array[286:297, 0:15]
classAcca_sellowianaY=array[286:297, 0]

classHydrangea_spX=array[297:308, 0:15]
classHydrangea_spY=array[297:308, 0]

classPseudosasa_japonicaX=array[308:319, 0:15]
classPseudosasa_japonicaY=array[308:319, 0]

classMagnolia_grandifloraX=array[319:330, 0:15]
classMagnolia_grandifloraY=array[319:330, 0]

classGeranium_spX=array[330:340, 0:15]
classGeranium_spY=array[330:340, 0]

subplot(2,3,1)
quercus_subber1=plt.scatter(classQuercus_suberX[:,1], classQuercus_suberX[:,2], color='purple')
salix1=plt.scatter(classSalix_atrocineraX[:,1], classSalix_atrocineraX[:,2], color='g')
populus_nigra1=plt.scatter(classPopulus_nigraX[:,1], classPopulus_nigraX[:,2], color='b')
alnus1=plt.scatter(classAlnus_spX[:,1], classAlnus_spX[:,2], color='r')
quercus_robur1=plt.scatter(classQuercus_roburX[:,1], classQuercus_roburX[:,2], color='black')
crataegus1=plt.scatter(classCrataegus_monogynaX[:,1], classCrataegus_monogynaX[:,2], color='yellow')
ilex_aquifolim1=plt.scatter(classIlex_aquifolimX[:,1], classIlex_aquifolimX[:,2], color='pink')
nerium1=plt.scatter(classNerium_oleanderX[:,1], classNerium_oleanderX[:,2], color='deeppink')
betula1=plt.scatter(classBetula_pubescensX[:,1], classBetula_pubescensX[:,2], color='khaki')
tilia1=plt.scatter(classTilia_tomentosaX[:,1], classTilia_tomentosaX[:,2], color='coral')
acer1=plt.scatter(classAcer_palmatumX[:,1], classAcer_palmatumX[:,2], color='peru')
cettis1=plt.scatter(classCeltis_spX[:,1], classCeltis_spX[:,2], color='lime')
corylus1=plt.scatter(classCorylus_avellanaX[:,1], classCorylus_avellanaX[:,2], color='aqua')
castanea1=plt.scatter(classCastanea_sativaX[:,1], classCastanea_sativaX[:,2], color='deepskyblue')
populus_alba1=plt.scatter(classPopulus_albaX[:,1], classPopulus_albaX[:,2], color='maroon')
primula1=plt.scatter(classPrimula_vulgarisX[:,1], classPrimula_vulgarisX[:,2], color='olive')
erodium1=plt.scatter(classErodium_spX[:,1], classErodium_spX[:,2], color='crimson')
bougainvilla1=plt.scatter(classBougainvillea_spX[:,1], classBougainvillea_spX[:,2], color='gray')
arisarum1=plt.scatter(classArisarum_vulgareX[:,1], classArisarum_vulgareX[:,2], color='mediumspringgreen')
enonymus1=plt.scatter(classEnonymus_japonicusX[:,1], classEnonymus_japonicusX[:,2], color='darkviolet')
ilex_perado1=plt.scatter(classIlex_perado_ssp_azoricaX[:,1], classIlex_perado_ssp_azoricaX[:,2], color='royalblue')
magnolia_soulangeana1=plt.scatter(classMagnolia_soulangeanaX[:,1], classMagnolia_soulangeanaX[:,2], color='silver')
buxus1=plt.scatter(classBuxus_sempervirensX[:,1], classBuxus_sempervirensX[:,2], color='fuchsia')
urtica1=plt.scatter(classUrtica_dioicaX[:,1], classUrtica_dioicaX[:,2], color='moccasin')
podocarpus1=plt.scatter(classPodocarpus_spX[:,1], classPodocarpus_spX[:,2], color='sandybrown')
acca1=plt.scatter(classAcca_sellowianaX[:,1], classAcca_sellowianaX[:,2], color='darkslategray')
hydrangea1=plt.scatter(classHydrangea_spX[:,1], classHydrangea_spX[:,2], color='mediumorchid')
pseudosasa1=plt.scatter(classPseudosasa_japonicaX[:,1], classPseudosasa_japonicaX[:,2], color='teal')
magnolia_grandiflora1=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,2], color='lightcoral')
geranium1=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,2], color='gold')

plt.xlabel('specimen-number')
plt.ylabel('eccentricity')


subplot(2,3,2)
quercus_subber2=plt.scatter(classQuercus_suberX[:,1], classQuercus_suberX[:,3], color='purple')
salix2=plt.scatter(classSalix_atrocineraX[:,1], classSalix_atrocineraX[:,3], color='g')
populus_nigra2=plt.scatter(classPopulus_nigraX[:,1], classPopulus_nigraX[:,3], color='b')
alnus2=plt.scatter(classAlnus_spX[:,1], classAlnus_spX[:,3], color='r')
quercus_robur2=plt.scatter(classQuercus_roburX[:,1], classQuercus_roburX[:,3], color='black')
crataegus2=plt.scatter(classCrataegus_monogynaX[:,1], classCrataegus_monogynaX[:,3], color='yellow')
ilex_aquifolim2=plt.scatter(classIlex_aquifolimX[:,1], classIlex_aquifolimX[:,3], color='pink')
nerium2=plt.scatter(classNerium_oleanderX[:,1], classNerium_oleanderX[:,3], color='deeppink')
betula2=plt.scatter(classBetula_pubescensX[:,1], classBetula_pubescensX[:,3], color='khaki')
tilia2=plt.scatter(classTilia_tomentosaX[:,1], classTilia_tomentosaX[:,3], color='coral')
acer2=plt.scatter(classAcer_palmatumX[:,1], classAcer_palmatumX[:,3], color='peru')
cettis2=plt.scatter(classCeltis_spX[:,1], classCeltis_spX[:,3], color='lime')
corylus2=plt.scatter(classCorylus_avellanaX[:,1], classCorylus_avellanaX[:,3], color='aqua')
castanea2=plt.scatter(classCastanea_sativaX[:,1], classCastanea_sativaX[:,3], color='deepskyblue')
populus_alba2=plt.scatter(classPopulus_albaX[:,1], classPopulus_albaX[:,3], color='maroon')
primula2=plt.scatter(classPrimula_vulgarisX[:,1], classPrimula_vulgarisX[:,3], color='olive')
erodium2=plt.scatter(classErodium_spX[:,1], classErodium_spX[:,3], color='crimson')
bougainvilla2=plt.scatter(classBougainvillea_spX[:,1], classBougainvillea_spX[:,3], color='gray')
arisarum2=plt.scatter(classArisarum_vulgareX[:,1], classArisarum_vulgareX[:,3], color='mediumspringgreen')
enonymus2=plt.scatter(classEnonymus_japonicusX[:,1], classEnonymus_japonicusX[:,3], color='darkviolet')
ilex_perado2=plt.scatter(classIlex_perado_ssp_azoricaX[:,1], classIlex_perado_ssp_azoricaX[:,3], color='royalblue')
magnolia_soulangeana2=plt.scatter(classMagnolia_soulangeanaX[:,1], classMagnolia_soulangeanaX[:,3], color='silver')
buxus2=plt.scatter(classBuxus_sempervirensX[:,1], classBuxus_sempervirensX[:,3], color='fuchsia')
urtica2=plt.scatter(classUrtica_dioicaX[:,1], classUrtica_dioicaX[:,3], color='moccasin')
podocarpus2=plt.scatter(classPodocarpus_spX[:,1], classPodocarpus_spX[:,3], color='sandybrown')
acca2=plt.scatter(classAcca_sellowianaX[:,1], classAcca_sellowianaX[:,3], color='darkslategray')
hydrangea2=plt.scatter(classHydrangea_spX[:,1], classHydrangea_spX[:,3], color='mediumorchid')
pseudosasa2=plt.scatter(classPseudosasa_japonicaX[:,1], classPseudosasa_japonicaX[:,3], color='teal')
magnolia_grandiflora2=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,3], color='lightcoral')
geranium2=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,3], color='gold')
plt.xlabel('specimen-number')
plt.ylabel('aspect-ratio')


subplot(2,3,3)
quercus_subber3=plt.scatter(classQuercus_suberX[:,1], classQuercus_suberX[:,4], color='purple')
salix3=plt.scatter(classSalix_atrocineraX[:,1], classSalix_atrocineraX[:,4], color='g')
populus_nigra3=plt.scatter(classPopulus_nigraX[:,1], classPopulus_nigraX[:,4], color='b')
alnus3=plt.scatter(classAlnus_spX[:,1], classAlnus_spX[:,4], color='r')
quercus_robur3=plt.scatter(classQuercus_roburX[:,1], classQuercus_roburX[:,4], color='black')
crataegus3=plt.scatter(classCrataegus_monogynaX[:,1], classCrataegus_monogynaX[:,4], color='yellow')
ilex_aquifolim3=plt.scatter(classIlex_aquifolimX[:,1], classIlex_aquifolimX[:,4], color='pink')
nerium3=plt.scatter(classNerium_oleanderX[:,1], classNerium_oleanderX[:,4], color='deeppink')
betula3=plt.scatter(classBetula_pubescensX[:,1], classBetula_pubescensX[:,4], color='khaki')
tilia3=plt.scatter(classTilia_tomentosaX[:,1], classTilia_tomentosaX[:,4], color='coral')
acer3=plt.scatter(classAcer_palmatumX[:,1], classAcer_palmatumX[:,4], color='peru')
cettis3=plt.scatter(classCeltis_spX[:,1], classCeltis_spX[:,4], color='lime')
corylus3=plt.scatter(classCorylus_avellanaX[:,1], classCorylus_avellanaX[:,4], color='aqua')
castanea3=plt.scatter(classCastanea_sativaX[:,1], classCastanea_sativaX[:,4], color='deepskyblue')
populus_alba3=plt.scatter(classPopulus_albaX[:,1], classPopulus_albaX[:,4], color='maroon')
primula3=plt.scatter(classPrimula_vulgarisX[:,1], classPrimula_vulgarisX[:,4], color='olive')
erodium3=plt.scatter(classErodium_spX[:,1], classErodium_spX[:,4], color='crimson')
bougainvilla3=plt.scatter(classBougainvillea_spX[:,1], classBougainvillea_spX[:,4], color='gray')
arisarum3=plt.scatter(classArisarum_vulgareX[:,1], classArisarum_vulgareX[:,4], color='mediumspringgreen')
enonymus3=plt.scatter(classEnonymus_japonicusX[:,1], classEnonymus_japonicusX[:,4], color='darkviolet')
ilex_perado3=plt.scatter(classIlex_perado_ssp_azoricaX[:,1], classIlex_perado_ssp_azoricaX[:,4], color='royalblue')
magnolia_soulangeana3=plt.scatter(classMagnolia_soulangeanaX[:,1], classMagnolia_soulangeanaX[:,4], color='silver')
buxus3=plt.scatter(classBuxus_sempervirensX[:,1], classBuxus_sempervirensX[:,4], color='fuchsia')
urtica3=plt.scatter(classUrtica_dioicaX[:,1], classUrtica_dioicaX[:,4], color='moccasin')
podocarpus3=plt.scatter(classPodocarpus_spX[:,1], classPodocarpus_spX[:,4], color='sandybrown')
acca3=plt.scatter(classAcca_sellowianaX[:,1], classAcca_sellowianaX[:,4], color='darkslategray')
hydrangea3=plt.scatter(classHydrangea_spX[:,1], classHydrangea_spX[:,4], color='mediumorchid')
pseudosasa3=plt.scatter(classPseudosasa_japonicaX[:,1], classPseudosasa_japonicaX[:,4], color='teal')
magnolia_grandiflora3=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,4], color='lightcoral')
geranium3=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,4], color='gold')

plt.xlabel('specimen-number')
plt.ylabel('elongation')
plt.legend((quercus_subber3, salix3, populus_nigra3, alnus3, quercus_robur3, crataegus3, ilex_aquifolim3, nerium3, betula3, tilia3, acer3, cettis3, corylus3, castanea3, populus_alba3, primula3, erodium3, bougainvilla3, arisarum3, enonymus3, ilex_perado3, magnolia_soulangeana3, buxus3, urtica3, podocarpus3, acca3, hydrangea3, pseudosasa3, magnolia_grandiflora3, geranium3), ('Quercus suber', 'Salix atrocinera', 'Populus nigra', 'Alnus sp.', 'Quercus robur', 'Crataegus monogyna', 'Ilex aquifolium', 'Nerium oleander', 'Betula pubescens', 'Tilia tomentosa', 'Acer palmatum', 'Celtis sp', 'Corylus avellana', 'Castanea sativa', 'Populus alba', 'Primula vulgaris', 'Erodium sp.', 'Bougainvillea sp.', 'Arisarum vulgare', 'Enonymus japonicus', 'Ilex perado ssp. azorica', 'Magnolia soulangeana', 'Buxus sempervirens', 'Urtica dioica', 'Podocarpus sp.', 'Acca sellowiana', 'Hydrangea sp.', 'Pseudosasa japonica', 'Magnolia grandiflora', 'Geranium sp.'))



subplot(2,3,4)
quercus_subber4=plt.scatter(classQuercus_suberX[:,1], classQuercus_suberX[:,5], color='purple')
salix4=plt.scatter(classSalix_atrocineraX[:,1], classSalix_atrocineraX[:,5], color='g')
populus_nigra4=plt.scatter(classPopulus_nigraX[:,1], classPopulus_nigraX[:,5], color='b')
alnus4=plt.scatter(classAlnus_spX[:,1], classAlnus_spX[:,5], color='r')
quercus_robur4=plt.scatter(classQuercus_roburX[:,1], classQuercus_roburX[:,5], color='black')
crataegus4=plt.scatter(classCrataegus_monogynaX[:,1], classCrataegus_monogynaX[:,5], color='yellow')
ilex_aquifolim4=plt.scatter(classIlex_aquifolimX[:,1], classIlex_aquifolimX[:,5], color='pink')
nerium4=plt.scatter(classNerium_oleanderX[:,1], classNerium_oleanderX[:,5], color='deeppink')
betula4=plt.scatter(classBetula_pubescensX[:,1], classBetula_pubescensX[:,5], color='khaki')
tilia4=plt.scatter(classTilia_tomentosaX[:,1], classTilia_tomentosaX[:,5], color='coral')
acer4=plt.scatter(classAcer_palmatumX[:,1], classAcer_palmatumX[:,5], color='peru')
cettis4=plt.scatter(classCeltis_spX[:,1], classCeltis_spX[:,5], color='lime')
corylus4=plt.scatter(classCorylus_avellanaX[:,1], classCorylus_avellanaX[:,5], color='aqua')
castanea4=plt.scatter(classCastanea_sativaX[:,1], classCastanea_sativaX[:,5], color='deepskyblue')
populus_alba4=plt.scatter(classPopulus_albaX[:,1], classPopulus_albaX[:,5], color='maroon')
primula4=plt.scatter(classPrimula_vulgarisX[:,1], classPrimula_vulgarisX[:,5], color='olive')
erodium4=plt.scatter(classErodium_spX[:,1], classErodium_spX[:,4], color='crimson')
bougainvilla4=plt.scatter(classBougainvillea_spX[:,1], classBougainvillea_spX[:,5], color='gray')
arisarum4=plt.scatter(classArisarum_vulgareX[:,1], classArisarum_vulgareX[:,5], color='mediumspringgreen')
enonymus4=plt.scatter(classEnonymus_japonicusX[:,1], classEnonymus_japonicusX[:,5], color='darkviolet')
ilex_perado4=plt.scatter(classIlex_perado_ssp_azoricaX[:,1], classIlex_perado_ssp_azoricaX[:,5], color='royalblue')
magnolia_soulangeana4=plt.scatter(classMagnolia_soulangeanaX[:,1], classMagnolia_soulangeanaX[:,5], color='silver')
buxus4=plt.scatter(classBuxus_sempervirensX[:,1], classBuxus_sempervirensX[:,5], color='fuchsia')
urtica4=plt.scatter(classUrtica_dioicaX[:,1], classUrtica_dioicaX[:,5], color='moccasin')
podocarpus4=plt.scatter(classPodocarpus_spX[:,1], classPodocarpus_spX[:,5], color='sandybrown')
acca4=plt.scatter(classAcca_sellowianaX[:,1], classAcca_sellowianaX[:,5], color='darkslategray')
hydrangea4=plt.scatter(classHydrangea_spX[:,1], classHydrangea_spX[:,5], color='mediumorchid')
pseudosasa4=plt.scatter(classPseudosasa_japonicaX[:,1], classPseudosasa_japonicaX[:,5], color='teal')
magnolia_grandiflora4=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,5], color='lightcoral')
geranium4=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,5], color='gold')

plt.xlabel('specimen-number')
plt.ylabel('solidity')


subplot(2,3,5)
quercus_subber5=plt.scatter(classQuercus_suberX[:,1], classQuercus_suberX[:,6], color='purple')
salix5=plt.scatter(classSalix_atrocineraX[:,1], classSalix_atrocineraX[:,6], color='g')
populus_nigra5=plt.scatter(classPopulus_nigraX[:,1], classPopulus_nigraX[:,6], color='b')
alnus5=plt.scatter(classAlnus_spX[:,1], classAlnus_spX[:,6], color='r')
quercus_robur5=plt.scatter(classQuercus_roburX[:,1], classQuercus_roburX[:,6], color='black')
crataegus5=plt.scatter(classCrataegus_monogynaX[:,1], classCrataegus_monogynaX[:,6], color='yellow')
ilex_aquifolim5=plt.scatter(classIlex_aquifolimX[:,1], classIlex_aquifolimX[:,6], color='pink')
nerium5=plt.scatter(classNerium_oleanderX[:,1], classNerium_oleanderX[:,6], color='deeppink')
betula5=plt.scatter(classBetula_pubescensX[:,1], classBetula_pubescensX[:,6], color='khaki')
tilia5=plt.scatter(classTilia_tomentosaX[:,1], classTilia_tomentosaX[:,6], color='coral')
acer5=plt.scatter(classAcer_palmatumX[:,1], classAcer_palmatumX[:,6], color='peru')
cettis5=plt.scatter(classCeltis_spX[:,1], classCeltis_spX[:,6], color='lime')
corylus5=plt.scatter(classCorylus_avellanaX[:,1], classCorylus_avellanaX[:,6], color='aqua')
castanea5=plt.scatter(classCastanea_sativaX[:,1], classCastanea_sativaX[:,6], color='deepskyblue')
populus_alba5=plt.scatter(classPopulus_albaX[:,1], classPopulus_albaX[:,6], color='maroon')
primula5=plt.scatter(classPrimula_vulgarisX[:,1], classPrimula_vulgarisX[:,6], color='olive')
erodium5=plt.scatter(classErodium_spX[:,1], classErodium_spX[:,6], color='crimson')
bougainvilla5=plt.scatter(classBougainvillea_spX[:,1], classBougainvillea_spX[:,6], color='gray')
arisarum5=plt.scatter(classArisarum_vulgareX[:,1], classArisarum_vulgareX[:,6], color='mediumspringgreen')
enonymus5=plt.scatter(classEnonymus_japonicusX[:,1], classEnonymus_japonicusX[:,6], color='darkviolet')
ilex_perado5=plt.scatter(classIlex_perado_ssp_azoricaX[:,1], classIlex_perado_ssp_azoricaX[:,6], color='royalblue')
magnolia_soulangeana5=plt.scatter(classMagnolia_soulangeanaX[:,1], classMagnolia_soulangeanaX[:,6], color='silver')
buxus5=plt.scatter(classBuxus_sempervirensX[:,1], classBuxus_sempervirensX[:,6], color='fuchsia')
urtica5=plt.scatter(classUrtica_dioicaX[:,1], classUrtica_dioicaX[:,6], color='moccasin')
podocarpus5=plt.scatter(classPodocarpus_spX[:,1], classPodocarpus_spX[:,6], color='sandybrown')
acca5=plt.scatter(classAcca_sellowianaX[:,1], classAcca_sellowianaX[:,6], color='darkslategray')
hydrangea5=plt.scatter(classHydrangea_spX[:,1], classHydrangea_spX[:,6], color='mediumorchid')
pseudosasa5=plt.scatter(classPseudosasa_japonicaX[:,1], classPseudosasa_japonicaX[:,6], color='teal')
magnolia_grandiflora5=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,6], color='lightcoral')
geranium5=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,6], color='gold')

plt.xlabel('specimen-number')
plt.ylabel('stochastic-convexity')


subplot(2,3,6)
quercus_subber6=plt.scatter(classQuercus_suberX[:,1], classQuercus_suberX[:,7], color='purple')
salix6=plt.scatter(classSalix_atrocineraX[:,1], classSalix_atrocineraX[:,7], color='g')
populus_nigra6=plt.scatter(classPopulus_nigraX[:,1], classPopulus_nigraX[:,7], color='b')
alnus6=plt.scatter(classAlnus_spX[:,1], classAlnus_spX[:,7], color='r')
quercus_robur6=plt.scatter(classQuercus_roburX[:,1], classQuercus_roburX[:,7], color='black')
crataegus6=plt.scatter(classCrataegus_monogynaX[:,1], classCrataegus_monogynaX[:,7], color='yellow')
ilex_aquifolim6=plt.scatter(classIlex_aquifolimX[:,1], classIlex_aquifolimX[:,7], color='pink')
nerium6=plt.scatter(classNerium_oleanderX[:,1], classNerium_oleanderX[:,7], color='deeppink')
betula6=plt.scatter(classBetula_pubescensX[:,1], classBetula_pubescensX[:,7], color='khaki')
tilia6=plt.scatter(classTilia_tomentosaX[:,1], classTilia_tomentosaX[:,7], color='coral')
acer6=plt.scatter(classAcer_palmatumX[:,1], classAcer_palmatumX[:,7], color='peru')
cettis6=plt.scatter(classCeltis_spX[:,1], classCeltis_spX[:,7], color='lime')
corylus6=plt.scatter(classCorylus_avellanaX[:,1], classCorylus_avellanaX[:,7], color='aqua')
castanea6=plt.scatter(classCastanea_sativaX[:,1], classCastanea_sativaX[:,7], color='deepskyblue')
populus_alba6=plt.scatter(classPopulus_albaX[:,1], classPopulus_albaX[:,7], color='maroon')
primula6=plt.scatter(classPrimula_vulgarisX[:,1], classPrimula_vulgarisX[:,7], color='olive')
erodium6=plt.scatter(classErodium_spX[:,1], classErodium_spX[:,7], color='crimson')
bougainvilla6=plt.scatter(classBougainvillea_spX[:,1], classBougainvillea_spX[:,7], color='gray')
arisarum6=plt.scatter(classArisarum_vulgareX[:,1], classArisarum_vulgareX[:,7], color='mediumspringgreen')
enonymus6=plt.scatter(classEnonymus_japonicusX[:,1], classEnonymus_japonicusX[:,7], color='darkviolet')
ilex_perado6=plt.scatter(classIlex_perado_ssp_azoricaX[:,1], classIlex_perado_ssp_azoricaX[:,7], color='royalblue')
magnolia_soulangeana6=plt.scatter(classMagnolia_soulangeanaX[:,1], classMagnolia_soulangeanaX[:,7], color='silver')
buxus6=plt.scatter(classBuxus_sempervirensX[:,1], classBuxus_sempervirensX[:,7], color='fuchsia')
urtica6=plt.scatter(classUrtica_dioicaX[:,1], classUrtica_dioicaX[:,7], color='moccasin')
podocarpus6=plt.scatter(classPodocarpus_spX[:,1], classPodocarpus_spX[:,7], color='sandybrown')
acca6=plt.scatter(classAcca_sellowianaX[:,1], classAcca_sellowianaX[:,7], color='darkslategray')
hydrangea6=plt.scatter(classHydrangea_spX[:,1], classHydrangea_spX[:,7], color='mediumorchid')
pseudosasa6=plt.scatter(classPseudosasa_japonicaX[:,1], classPseudosasa_japonicaX[:,7], color='teal')
magnolia_grandiflora6=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,7], color='lightcoral')
geranium6=plt.scatter(classMagnolia_grandifloraX[:,1], classMagnolia_grandifloraX[:,7], color='gold')

plt.xlabel('specimen-number')
plt.ylabel('isoperimetric-factor')


show()

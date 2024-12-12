import pydicom
import matplotlib.pyplot as plt
from datetime import datetime

# Lendo o arquivo DICOM
ds = pydicom.dcmread("C:/Users/My/Desktop/dicom/dicom.dcm")

#print(ds)
# Acessando informações
print("Nome do paciente:", ds.PatientName.family_name, ds.PatientName.given_name)
print("Id do paciente:", ds.PatientID)
print("Número de série do dispositivo", ds.DeviceSerialNumber)

create_date = ds.InstanceCreationDate # 20241211
create_date = create_date[:4] + '-' + create_date[4:]
create_date = create_date[:7] + '-' + create_date[7:]

create_time = ds.InstanceCreationTime # 050623.5780
create_time = create_time[:2] + ':' + create_time[2:]
create_time = create_time[:5] + ':' + create_time[5:]

create_datetime = f"{create_date} {create_time}"

create_datetime_obj = datetime.strptime(create_datetime, "%Y-%m-%d %H:%M:%S.%f")
create_dd_mm_yyyy = create_datetime_obj.strftime("%d/%m/%Y %H:%M:%S")

print("Criado em:", create_dd_mm_yyyy)
#print("Data de aquisição:", ds.AcquisitionDate)
#print("Matriz de pixels:", ds.pixel_array.shape)


# Fazer funcionar a leitura de imagens
# Extraindo a matriz de pixels
#pixel_data = ds.pixel_array

#plt.imshow(pixel_data, cmap=plt.cm.gray)
#plt.axis('off')
#plt.show()
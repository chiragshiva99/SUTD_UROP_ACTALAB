from django.core import validators
from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import FileExtensionValidator

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField("Full Name", max_length = 250)

    def __str__(self):
        return self.full_name


Instrument_Choices = (
    ('Linkam - Optical spectra vs Temperature', 'Linkam- Optical spectra vs Temperature'),
    ('Linkam - Reflectance vs Temperature', 'Linkam- Reflectance vs Temperature'),
    ('Linkam - Video of crystallisation (formed by composing images)', 'Linkam - Video of crystallisation (formed by composing images)'),
    ('Vector Network Analyser (VNA)- Permittivity', 'Vector Network Analyser (VNA)- Permittivity'),
    ('Vector Network Analyser (VNA)- Permeability', 'Vector Network Analyser (VNA)- Permeability'),
    ('Four Point Probe- Resistivity', 'Four Point Probe- Resistivity'),
    ('Four Point Probe- Resistivity vs temperature', 'Four Point Probe- Resistivity vs temperature'),
    ('Static Tester (Optics Lab)- Switching times (Reflectivity vs Time and Power)', 'Static Tester (Optics Lab)- Switching times (Reflectivity vs Time and Power)'),
    ('Transient Grating Spectrometer- Elastic Tensor', 'Transient Grating Spectrometer- Elastic Tensor'),
    ('Transient Grating Spectrometer- Thermal diffusivity', 'Transient Grating Spectrometer- Thermal diffusivity'),
    ('Raman Microscope- Intensity vs Energy', 'Raman Microscope- Intensity vs Energy'),
    ('Raman Microscope- Intensity vs Frequency', 'Raman Microscope- Intensity vs Frequency'),
    ('Perkin Elmer Spectrometer- Reflectivity vs wavelength', 'Perkin Elmer Spectrometer- Reflectivity vs wavelength'),
    ('Perkin Elmer Spectrometer- Transmissivity vs wavelength', 'Perkin Elmer Spectrometer- Transmissivity vs wavelength'),
    ('Scanning Electron Microscope- Images', 'Scanning Electron Microscope- Images'),
    ('SEM Energy dispersive X-ray Analysis (EDX)- Fluorescent intensity vs energy', 'SEM Energy dispersive X-ray Analysis (EDX)- Fluorescent intensity vs energy'),
    ('SEM Electron Backscattering diffraction (EBS)- ?', 'SEM Electron Backscattering diffraction (EBS)- ?'),
    ('X-ray Diffractometers- Intensity vs angle', 'X-ray Diffractometers- Intensity vs angle'),
    ('X-ray Diffractometers- X-ray reflectivity (thickness, density, roughness)', 'X-ray Diffractometers- X-ray reflectivity (thickness, density, roughness)'),
    ('Ellipsometer- Refractive index vs wavelength', 'Ellipsometer- Refractive index vs wavelength'),
    ('Atomic Force Microscope (AFM)- Thickness vs length', 'Atomic Force Microscope (AFM)- Thickness vs length'),
    ('Atomic Force Microscope (AFM)- Map of roughness', 'Atomic Force Microscope (AFM)- Map of roughness'),
)


class DetailsOfDataCollection(models.Model):
    
    operator = models.CharField(max_length=250)
    sample_id = models.CharField("Sample ID", max_length = 250)
    comments = models.TextField()
    composition = models.CharField(max_length = 254)
    upload_data = models.FileField(upload_to= 'instrument_datatype') 
    instru_datatype = models.CharField("Instrument Datatype", max_length=250, choices= Instrument_Choices, default= 'Linkam- Optical spectra vs Temperature')
    
    def str(self):
        return self.operator()

class TxtFile(models.Model):
    name =  models.CharField(max_length=254)
    material_name = models.CharField("Material Name", max_length=254)
    txtfile = models.FileField("Data File (.txt only)", upload_to = "txtfiles_folder", validators=[FileExtensionValidator(allowed_extensions=['txt'])])

    def str(self):
        return self.txtfile 

class MaterialList(models.Model):
    material = models.CharField(max_length=250)
    source_of_data = models.CharField("Source of Data", max_length=250)
    date_added = models.DateField("Material Created On (YYYY-MM-DD)")

    def str(self):
        return self.material()

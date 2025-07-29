# Estructura de Carpetas - Proyecto Monitoreo Forestal

```
📁 MonitoreoForestal_SOP/
│
├── 📁 config/
│   ├── config.json                    # Configuración general del proyecto
│   ├── credentials/
│   │   ├── gee_service_account.json   # Credenciales Google Earth Engine
│   │   └── arcgis_credentials.json    # Credenciales ArcGIS
│   └── templates/
│       ├── metadata_template.xml      # Plantilla metadatos
│       └── report_template.html       # Plantilla reportes
│
├── 📁 data/
│   ├── 📁 raw/                        # Datos originales (NUNCA modificar)
│   │   ├── 📁 vectorial/
│   │   │   ├── 📁 bosques/
│   │   │   │   ├── bosques_2023.shp
│   │   │   │   ├── bosques_2024.shp
│   │   │   │   └── README.txt         # Descripción de datos
│   │   │   ├── 📁 areas_protegidas/
│   │   │   ├── 📁 limites_administrativos/
│   │   │   ├── 📁 hidrografia/
│   │   │   └── 📁 infraestructura/
│   │   ├── 📁 raster/
│   │   │   ├── 📁 dem/
│   │   │   ├── 📁 landsat/
│   │   │   └── 📁 sentinel/
│   │   └── 📁 tabular/
│   │       ├── inventario_forestal.csv
│   │       └── especies_endemicas.xlsx
│   │
│   ├── 📁 processed/                  # Datos procesados/limpios
│   │   ├── 📁 vectorial_clean/
│   │   │   ├── 📁 bosques_validated/
│   │   │   └── 📁 areas_protegidas_clean/
│   │   ├── 📁 raster_processed/
│   │   └── 📁 tabular_clean/
│   │
│   ├── 📁 temp/                       # Archivos temporales
│   │   ├── 📁 gee_downloads/
│   │   ├── 📁 arcgis_temp/
│   │   └── 📁 python_cache/
│   │
│   └── 📁 outputs/                    # Resultados finales
│       ├── 📁 intersections/
│       │   ├── 📁 2024/
│       │   │   ├── 📁 enero/
│       │   │   ├── 📁 febrero/
│       │   │   └── 📁 [mes]/
│       │   └── 📁 2023/
│       ├── 📁 analysis_results/
│       ├── 📁 maps/
│       │   ├── 📁 pdf/
│       │   ├── 📁 png/
│       │   └── 📁 mxd_aprx/
│       └── 📁 statistics/
│
├── 📁 scripts/
│   ├── 📁 python/
│   │   ├── 📁 core/                   # Módulos principales
│   │   │   ├── __init__.py
│   │   │   ├── data_validator.py      # Validación de datos
│   │   │   ├── vector_processor.py    # Procesamiento vectorial
│   │   │   ├── gee_connector.py       # Conexión con GEE
│   │   │   └── report_generator.py    # Generación reportes
│   │   ├── 📁 workflows/              # Flujos de trabajo específicos
│   │   │   ├── daily_validation.py
│   │   │   ├── weekly_intersection.py
│   │   │   ├── monthly_analysis.py
│   │   │   └── quarterly_report.py
│   │   ├── 📁 utilities/              # Utilidades auxiliares
│   │   │   ├── file_manager.py
│   │   │   ├── logger_config.py
│   │   │   └── email_sender.py
│   │   └── main_processor.py          # Script principal
│   │
│   ├── 📁 arcgis/
│   │   ├── 📁 toolboxes/
│   │   │   └── ForestAnalysis.atbx
│   │   ├── 📁 models/
│   │   │   ├── buffer_analysis.aprx
│   │   │   └── intersection_model.aprx
│   │   └── 📁 python_scripts/
│   │       ├── arcpy_intersections.py
│   │       └── advanced_spatial_analysis.py
│   │
│   ├── 📁 gee/
│   │   ├── forest_change_detection.js
│   │   ├── ndvi_time_series.js
│   │   ├── sentinel_preprocessing.js
│   │   └── export_to_drive.js
│   │
│   └── 📁 batch/
│       ├── setup_environment.bat      # Windows
│       ├── setup_environment.sh       # Linux/Mac
│       ├── daily_routine.bat
│       └── backup_data.bat
│
├── 📁 documentation/
│   ├── 📁 sop/                        # Procedimientos Operativos Estándar
│   │   ├── data_validation_sop.md
│   │   ├── vector_intersection_sop.md
│   │   ├── quality_control_sop.md
│   │   └── report_generation_sop.md
│   ├── 📁 technical/
│   │   ├── system_requirements.md
│   │   ├── installation_guide.md
│   │   └── troubleshooting.md
│   ├── 📁 metadata/
│   │   ├── data_dictionary.xlsx
│   │   └── coordinate_systems.md
│   └── 📁 user_manuals/
│       ├── beginner_guide.pdf
│       └── advanced_workflows.pdf
│
├── 📁 logs/
│   ├── 📁 daily/
│   │   ├── 2024-07-22.log
│   │   └── [fecha].log
│   ├── 📁 error/
│   │   └── error_2024-07.log
│   ├── 📁 processing/
│   │   └── processing_2024-07.log
│   └── system.log                     # Log principal del sistema
│
├── 📁 reports/
│   ├── 📁 daily/
│   │   ├── 📁 2024/
│   │   │   ├── 📁 julio/
│   │   │   │   ├── daily_report_2024-07-22.html
│   │   │   │   └── daily_report_2024-07-22.pdf
│   │   │   └── 📁 [mes]/
│   │   └── 📁 templates/
│   ├── 📁 weekly/
│   ├── 📁 monthly/
│   ├── 📁 quarterly/
│   └── 📁 annual/
│
├── 📁 backup/
│   ├── 📁 automated/                  # Respaldos automatizados
│   │   ├── 📁 daily/
│   │   ├── 📁 weekly/
│   │   └── 📁 monthly/
│   └── 📁 manual/                     # Respaldos manuales
│
├── 📁 git_config/
│   ├── .gitignore                     # Archivos a ignorar por Git
│   ├── .gitattributes                 # Atributos Git (para archivos grandes)
│   └── 📁 hooks/                      # Git hooks personalizados
│       ├── pre-commit
│       └── post-commit
│
├── 📁 testing/
│   ├── 📁 unit_tests/
│   │   ├── test_data_validator.py
│   │   ├── test_vector_processor.py
│   │   └── test_gee_connector.py
│   ├── 📁 integration_tests/
│   ├── 📁 sample_data/               # Datos de muestra para testing
│   └── run_all_tests.py
│
├── 📁 environments/
│   ├── requirements.txt              # Dependencias Python
│   ├── environment.yml               # Ambiente Conda
│   ├── arcgis_extensions.txt         # Extensiones ArcGIS necesarias
│   └── 📁 docker/                    # Containerización (opcional)
│       ├── Dockerfile
│       └── docker-compose.yml
│
└── 📁 resources/
    ├── 📁 symbols/                   # Simbologías para mapas
    │   ├── forest_symbols.style
    │   └── protected_areas.lyrx
    ├── 📁 projections/               # Archivos de proyección
    ├── 📁 fonts/                     # Fuentes para mapas
    └── 📁 icons/                     # Iconos para interfaces

# Archivos en la Raíz del Proyecto:
├── README.md                         # Descripción del proyecto
├── CHANGELOG.md                      # Registro de cambios
├── LICENSE                           # Licencia del proyecto
├── .gitignore                        # Archivos ignorados por Git
├── requirements.txt                  # Dependencias principales
├── environment.yml                   # Ambiente Conda
├── setup.py                          # Instalación del paquete
└── main.py                           # Script de ejecución principal
```

## Convenciones de Nomenclatura:

### Para Archivos de Datos:
```
[tipo_dato]_[año]_[mes/fecha]_[version].[extensión]
Ejemplo: bosques_2024_julio_v01.shp
```

### Para Scripts:
```
[función]_[herramienta]_[version].py
Ejemplo: intersection_arcgis_v02.py
```

### Para Reportes:
```
[tipo_reporte]_[fecha]_[version].[extensión]
Ejemplo: monthly_report_2024-07_v01.pdf
```

## Archivos Especiales Recomendados:

### 📄 .gitignore personalizado:
```
# Datos temporales
01_DATA/TEMP/
04_LOGS/*.log
06_BACKUP/automated/

# Archivos ArcGIS
*.lock
*.sr.lock
*.gdb/

# Python
__pycache__/
*.pyc
*.pyo
.pytest_cache/

# Credenciales
00_CONFIG/credentials/

# Archivos grandes (usar Git LFS)
*.tif
*.img
*.sid
```

### 📄 Estructura para cada carpeta RAW:
Cada subcarpeta de datos debe incluir:
- `README.txt` - Descripción de los datos
- `metadata.xml` - Metadatos completos
- `source_info.txt` - Información de la fuente

Esta estructura te permite:
- **Escalabilidad**: Fácil agregar nuevos tipos de datos
- **Trazabilidad**: Cada proceso está documentado
- **Colaboración**: Estructura clara para equipos
- **Automatización**: Rutas predecibles para scripts
- **Respaldo**: Sistema organizado de backups
- **Control de calidad**: Separación clara entre datos originales y procesados
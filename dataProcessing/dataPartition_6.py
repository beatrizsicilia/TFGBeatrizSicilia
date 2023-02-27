import pandas as pd

cities = ["NewYork_US", "Tokyo_JP"]

for i in cities:
    file_name  = "dataProcessing\\intermediateFiles\\" + i + "finalVersion.txt" 

    datos = pd.read_csv(file_name, sep='\t', header=None)

    #sorting by timestamp, menor a mayor. 
    datos_ordered = datos.sort_values(2)

    #TRAIN:
    n_records_train = int(0.7 * len(datos_ordered.index))
    # Select the first 70% of the records
    train_df = datos_ordered.iloc[:n_records_train]
    file_name = "subsets\\" + i + "_train.txt"
    train_df.to_csv(file_name, sep='\t', index=False, header=None)

    #VALIDATION:
    n_records_validation = int(0.1 * len(datos_ordered.index)) + n_records_train
    # Select the next 10% of data.
    validation_df= datos_ordered.iloc[n_records_train:n_records_validation]
    file_name = "subsets\\" +i + "_validation.txt"
    validation_df.to_csv(file_name, sep='\t', index=False, header=None)

    #TEST: 
    n_records_test = int(0.2 * len(datos_ordered.index)) + n_records_validation
    # Select the upper 20% of data.
    test_df= datos_ordered.iloc[n_records_validation:n_records_test]
    file_name = "subsets\\"+ i + "_test.txt"
    test_df.to_csv(file_name, sep='\t', index=False, header=None)
    


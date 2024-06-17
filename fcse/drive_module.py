



ree = "1AidBHDjC0QrafhxekBe5SFtqxJzL4Nli"
ree_texts = '1cGFKS7-vIXZi4T6YaVoQrcW6hrQNCtly'
ra = "11cOTl6N5m9whAcPrQnCGksNRAE02GfGC"
kor = "1YsGrSdHHRLRvV2bBvQuWNlnWfsm0AMC_"
ming = "11sbPdj5jBxVf76ddkIvCjU3ASBKdlKT4"
rmf = '17NsNIO9k4v2IU1x-fmRqpluWEv_ATcTJ'
fcse = '133H_cn0urMFlVOh-iSeShe_6wwVNZrz2'
file_name = rf"C:\Users\91833\Downloads\{novel}_{stop_number}.epub"

upload_f_to_g_drive(file_name=up_file_path, folder_id=ree_texts)

txt_to_epub(up_file_path)
upload_f_to_g_drive(file_name=file_name, folder_id=fcse)
from selenium import webdriver
from time import sleep

database = {
    "Account": {
        "NIM": "",
        "Password": ""
    },
    "URL": {
        "MOLS": "https://mols.unmul.ac.id/mahasiswa/login",
        "Class": {
            "SD": "https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/sistem-digital-a-2020/7075/jRGbzs/index",
            "SO": "https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/sistem-operasi/7208/FJTddP/index",
            "FGE": "https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/fge-ab2020/8099/bGqFnp/index",
            "APL": "https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/algoritma-lanjut/8593/T029KF/index",
            "ISBD": "https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/isbd-if-abc-feb-kelas-perbaikan/8631/JXKyFl/index",
            "MTK": "https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/matematika-informatika-a-2020/8648/dhYMF8/index",
            "JKK": "https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/jaringan-dan-keamanan-komputer-ac20/8810/iUpTbh/index",
            "PBO": "https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/pbo-gabungan-2020/7791/iByGIW/index"
        }
    }
}

def mols_login():
    browser.get(database["URL"]["MOLS"])
    sleep(1)
    browser.find_element_by_id("nim").send_keys(database["Account"]["NIM"])
    sleep(1)
    browser.find_element_by_id("password").send_keys(database["Account"]["Password"])
    sleep(1)
    browser.find_element_by_id("btn-login").click()
    sleep(3)

def mols_hadir(url):
    browser.get(url)
    sleep(1)
    try:
        browser.find_element_by_class_name("btn.btn-outline-success.btn-rounded.btn-absent").click()
        sleep(3)
    except:
        sleep(1)

if __name__ == "__main__":
    browser = webdriver.Edge("msedgedriver.exe")
    mols_login()
    for url in database["URL"]["Class"].values():
        mols_hadir(url)
    browser.close()

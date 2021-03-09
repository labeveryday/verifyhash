# verifyhash

This is a script to verify your file hash. Use this script to learn the basics of python.

>Note: Currently script is fully functional but is in the process of updating linting, documentation and functionality.

## Download the Code

To get started: Download the code and cd to the `verifyhash` directory

```bash
git clone https://github.com/labeveryday/verifyhash.git
cd verifyhash
```

## Python Virtual Environment

When executing python code or installing python packages you should get into the practice of creating and managing python virtual environments.
This will allow you to run different versions of a python library while avoiding software version conflicts. My preferred tool for python virtual environments is [venv](https://docs.python.org/3/library/venv.html)
There are many other tools available. Remember to explore and find the one that works best for you.

**On Linux or Mac**

```python
python3 -m venv venv
source venv/bin/activate
```

**On Windows**

```cmd
python3 -m venv venv
.\venv\Scripts\activate.bat
```

## Install project requirements

Once you have your virtual environment setup and activated you will need to install your python packages. One way to do this is by doing `pip install <python_package_name>`. For this project use the example listed below. It will installed the required libraries and dependencies for this specific project.

```bash
pip install -r requirements.txt
```

## Example: Script in action

Now that the required dependencies are installed and updated you can now execute the script.

**Successful Hash Match**

```bash
(venv) duan@ubuntu verifyhash$ python main.py
Enter verified hash: ffa809e986ce58c0809d9d4feb556970b6bd87c4db4087490473eed8d67f44d6
Enter hashtype: sha256

                                   -------------------- FILEHASH RESULTS -------------------- 

                                        ********** ✅ Success HASH MATCH!!! ✅ **********
+---------------------------------------------------------+------------------------------------------------------------------+
|                        FileName                         |                         sha256 FileHash                          |
+---------------------------------------------------------+------------------------------------------------------------------+
| Downloaded File: DevNet.pdf                             | ffa809e986ce58c0809d9d4feb556970b6bd87c4db4087490473eed8d67f44d6 |
| Verified Hash:                                          | ffa809e986ce58c0809d9d4feb556970b6bd87c4db4087490473eed8d67f44d6 |
+---------------------------------------------------------+------------------------------------------------------------------+

 Press enter to exit

```

**FAILED Hash** 

```bash
Enter verified hash: f2f7a2a6c083ed376f2e7f21f6194571bf5e143ab3032849075ca64011fcb53e
Enter hashtype: sha256

                                   -------------------- FILEHASH RESULTS -------------------- 

                                  ********** ❌ FAILED!!!! HASH DOES NOT MATCH ❌ **********


+---------------------------------------------------------+------------------------------------------------------------------+
|                        FileName                         |                         sha256 FileHash                          |
+---------------------------------------------------------+------------------------------------------------------------------+
| Downloaded File: DevNet.pdf                             | f2f7a2a6c083ed376f2e7f21f6194571bf5e143ab3032849075ca64011fcb53e |
| Verified Hash:                                          | ffa809e986ce58c0809d9d4feb556970b6bd87c4db4087490473eed8d67f44d6 |
+---------------------------------------------------------+------------------------------------------------------------------+

 Press enter to exit
```

### About me

Introverted Network Automation Engineer that is changing lives as a Developer Advocate for Cisco DevNet. Pythons scripts are delicious. Especially at 2am on a Saturday night.

My hangouts:

- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)

- [Twitter](https://twitter.com/labeveryday)

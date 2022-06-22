
# startup-automation

This project was created to automate the process of starting often used software after a logon on your system. 
You can personalise it however you want. It also automates the process of organising the downloads-directory after downloading files. 

## Installation
Install the packages with pip

```bash
  pip install -r requirements.txt
```
    
After this you need to search for the windows-apps you want to start. This is easy to do with PowerShell. 

&nbsp;
### Search for apps to start
```
  get-StartApps
```

This will give you an App-ID as output. Search for the apps you want to open with the software. 
As an alternative you can start the apps with the directory-path. Just search for the main-.exe and copy the path. 

&nbsp;

### Configure the apps to start
The configuration is in the following file ``` startup.pyw ``` 
To configure the apps to start with the software you'll have to edit or copy the following line (in this case I want notion to start): 
```
  os.system(r'start explorer shell:appsfolder\notion.id')
```

If you want a app with the directory-path to start, copy or edit the following line (in this case I want to start VSCode with the software):
```
  subprocess.call(r'C:\Users\Pasca\AppData\Local\Programs\Microsoft VS Code\\code.exe')
```

&nbsp;
### Configure the key (trigger) the software should start at

To configure the key you want the software to start with, you'll have to edit the the following line: 

```
  if key == Key.pause:
```
In this case the key is "pause", you can change it to whatever you want to. 

&nbsp;

### Autostart configuration
This is quiet simple, to use the software in the autostart you just need to send shortcuts to your desktop. 
Run WIN + R and enter the following line:
```
  shell:common startup
```

Paste your shortcuts into this and they will start with your logon. 
## FAQ

#### Is there a way to contribute to this project?

Yes of course. Just read the point "contributing" below. 

#### Something is unclear in this small documentation, what should I do?

Just create a issue, we will look at this asap and help you with your problems. 


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## License

[MIT](https://choosealicense.com/licenses/mit/)


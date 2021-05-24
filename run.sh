pip3 install requests
if ! type screen >/dev/null 2>&1; then
    echo 'screen 未安装,准备安装screen';
    sudo apt install screen;
    else
      screen -S AutoLogin &&
      python3 AutoLogin.py;
fi

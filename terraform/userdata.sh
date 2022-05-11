#!/bin/bash


export DEBIAN_FRONTEND=noninteractive

# add hashi stuff
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=$(dpkg --print-architecture)] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y nmap bzip2 netcat net-tools git htop sysstat iotop vim-nox docker-ce docker-ce-cli docker-ce-rootless-extras docker-compose docker-scan-plugin python3-docker python3-dockerpty terraform vault

HM=/home/ubuntu


# add environment
cd $HM
git clone https://github.com/jacobm3/gbin.git
chmod +x gbin/*

echo '. ~/gbin/jacobrc'  >> ${HM}/.bashrc

sudo chown -R $USER:$USER $HM

cd ${HM}/gbin && sudo cp pg ng /usr/local/bin

cd $HM && mkdir -p .vim/colors 
cat > .vim/colors/jacobm3.vim <<EOF
set background=dark
hi clear
if exists("syntax_on")
  syntax reset
endif
let colors_name = "jacobm3"
hi Normal ctermbg=233 ctermfg=253
hi ErrorMsg         term=standout   ctermbg=DarkRed ctermfg=White
hi LineNr                   term=underline ctermfg=darkgrey
hi Question         term=standout ctermfg=LightGreen
hi Search                   term=reverse ctermbg=Yellow ctermfg=Black
hi WarningMsg   term=standout ctermfg=grey
hi WildMenu                 term=standout ctermbg=Yellow ctermfg=Black
hi Folded                   term=standout ctermbg=LightGrey ctermfg=grey
hi FoldColumn   term=standout ctermbg=LightGrey ctermfg=grey
hi Comment           ctermfg=246
hi String            ctermfg=081
hi Statement         ctermfg=119
hi Keyword           ctermfg=21
hi Include           ctermfg=21
hi PreCondit         ctermfg=21
hi Function          ctermfg=165
hi Constant         ctermfg=21
hi Define         ctermfg=165
hi Special          ctermfg=21
if &t_Co > 8
  hi Statement  ctermfg=21
endif
hi Ignore                   ctermfg=LightGrey

EOF

cat > ${HM}/.vimrc <<EOF
set number
set ts=4
set autoindent
set expandtab
set tabstop=4
set sw=4
colorscheme jacobm3
syntax on
EOF


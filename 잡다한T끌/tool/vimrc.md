
``` 
set shell=/bin/zsh

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'nanotech/jellybeans.vim' " 테마
Plugin 'scrooloose/nerdtree'
Plugin 'majutsushi/tagbar'      " 클래스와 메서드총정리( brew 에서 ctags 설치해야O함)
Plugin 'craigemery/vim-autotag'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'airblade/vim-gitgutter' " vim with git status(added, modified, and removed lines
Plugin 'tpope/vim-fugitive' " vim with git command(e.g., Gdiff)
Plugin 'vim-airline/vim-airline' " vim status bar
Plugin 'vim-airline/vim-airline-themes'
Plugin 'blueyed/vim-diminactive'  
Plugin 'Raimondi/delimitMate'   " 괄호 자동 완성
Plugin 'plasticboy/vim-markdown' " 마크다운지원
Plugin 'nvim-lua/plenary.nvim'
Plugin 'nvim-telescope/telescope.nvim', { 'tag': '0.1.6' }
Plugin 'renerocksai/telekasten.nvim'
call vundle#end()    

set t_Co=256

" for indent guide
let g:indentguides_tabchar = '|'
let g:indent_guides_enable_on_vim_startup = 1
let g:indent_guides_start_level=2
let g:indent_guides_guide_size=1

" for vim-airline
let g:airline#extensions#tabline#enabled = 1 " turn on buffer list
let g:airline_theme='hybrid'
set laststatus=2 " turn on bottom bar
let mapleader = "."


" 기본설정
set hidden      		" buffer가 저장되있지 않아도 swith
set nocompatible
set clipboard=unnamedplus
set number      		" 줄 넘버
set autoindent         	" 자동 들여쓰기
set smartindent     	" 스마트한 들여쓰기
set shiftwidth=4    	" >>, <<로 들여쓰기 칸
set tabstop=4       	" 탭 4칸
set nolist      		" 탭문자 원래대로
set wrap        		" 자동으로 다음행 넘어가기
set nobackup        	" 백업파일 만들지 않기
set bs=indent,eol,start " 백스페이스 사용
set nocp            	" vim 전용기능
set tenc=utf-8      	" 터미널 인코딩
set ruler               " 화면 우측 하단에 현재 커서의 위치(줄,칸) 표시
set encoding=utf-8
set fileencodings=utf-8,cp949
set hlsearch            " 검색어 강조, set hls 도 가능
set mouse=a     		" vim에서 마우스 사용
set autochdir       	" 실행파일의 경로로 자동 이동
filetype on
highlight Comment term=bold cterm=bold ctermfg=4
syntax enable           " 문법 하이라이트
colorscheme jellybeans 


" key mapping
nmap <leader>t :Tagbar<CR>  
nmap <leader>n :NERDTree<CR>  
nmap <leader>q :bp<CR>
nmap <leader>w :bn<CR>

" key mapping for telescope
nmap <leader>ff <cmd>Telescope find_files<cr>
nmap <leader>fg <cmd>Telescope live_grep<cr>
nmap <leader>fb <cmd>Telescope buffers<cr>
nmap <leader>fh <cmd>Telescope help_tags<cr>
nmap <leader>fo <cmd>Telescope oldfiles<cr>

" key mapping for telekasten
```
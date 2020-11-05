# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['pyRevit_installer.py'],
             pathex=[],
             binaries=[
                ( 'LibGit2Sharp.dll', '.' ),
                ( 'git2-106a5f2.dll', '.' )
             ],
             datas= [ ('rgb.txt', 'colorful\\data\\' ) ],
             hiddenimports=['clr'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='pyRevit_installer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

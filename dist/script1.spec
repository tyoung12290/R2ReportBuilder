# -*- mode: python -*-

block_cipher = None


a = Analysis(['script1.py'],
             pathex=['C:\\Users\\tyoung\\Documents\\Udemy\\Python\\R2_ReportBuilder\\dist'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='script1',
          debug=True,
          strip=False,
          upx=False,
          console=True )

gnome = import('gnome')

gnome.compile_resources(
  'nautilus-create-desktop-entry', 'nautilus-create-desktop-entry.gresource.xml',
  gresource_bundle: true,
  install_dir : pkgdata_dir,
  install: true
)

metafile = meson.project_name() + '.metainfo.xml'
i18n.merge_file(
  input: metafile + '.in',
  output: metafile,
  po_dir: '../po',
  install: true,
  install_dir : join_paths(get_option('datadir'), 'metainfo')
)

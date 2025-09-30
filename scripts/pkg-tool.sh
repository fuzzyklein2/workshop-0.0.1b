# pkg-config --cflags --libs gtkmm-4.0 gtest > data/pkg-config.out
pkg-config --cflags --libs $(../../scripts/get_packages.py) > data/pkg-config.out
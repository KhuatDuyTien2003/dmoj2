#!/bin/sh

# Kiểm tra xem sass có được cài đặt không
if ! command -v sass > /dev/null; then
  echo 'Error: sass is not installed.' >&2
  exit 1
fi

# Kiểm tra xem postcss có được cài đặt không
if ! command -v postcss > /dev/null; then
  echo 'Error: postcss is not installed.' >&2
  exit 1
fi

# Kiểm tra xem autoprefixer có được cài đặt không
if ! command -v autoprefixer > /dev/null; then
  echo 'Error: autoprefixer is not installed.' >&2
  exit 1
fi

# Di chuyển vào thư mục chứa script
cd "$(dirname "$0")" || exit 1

# Hàm xử lý biên dịch SCSS và PostCSS
build_style() {
  local style_name=$1
  local output_dir=$2

  echo "Creating $style_name style..."
  
  # Kiểm tra xem thư mục đích đã tồn tại chưa
  mkdir -p "$output_dir"

  # Sao chép file biến SCSS tương ứng
  cp "resources/vars-$style_name.scss" "resources/vars.scss"

  # Biên dịch SCSS
  sass resources:sass_processed

  # Xử lý CSS với PostCSS và Autoprefixer
  postcss sass_processed/*.css --use autoprefixer --dir "$output_dir"
}

# Gọi hàm để xử lý hai kiểu theme
build_style 'default' 'resources'
build_style 'dark' 'resources/dark'

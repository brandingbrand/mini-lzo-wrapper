{
  "targets": [
    {
      "target_name": "lzo",
      "sources": ["src/minilzo/minilzo.cc", "src/lzo.cc"],
      "cflags!": ["-fno-exceptions"],
      "cflags_cc!": ["-fno-exceptions"],
      "conditions": [
        ["OS==\"mac\"", {
          "xcode_settings": {
            "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
          }
        }]
      ]
    }
  ]
}

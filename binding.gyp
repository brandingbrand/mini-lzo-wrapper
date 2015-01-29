{
  'targets': [
    {
      'target_name': 'lzo',
      'sources': [ 'src/minilzo/minilzo.cc', 'src/lzo.cc' ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ]
    }
  ]
}

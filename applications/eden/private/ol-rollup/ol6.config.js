// Provides olgm (Google Maps) & ol-layerswitcher

import cjs from '@rollup/plugin-commonjs';
import node from '@rollup/plugin-node-resolve';
import {terser} from 'rollup-plugin-terser';

const production = !process.env.ROLLUP_WATCH;

export default {
  input: 'ol6.js',
  output: [
    {file: 'ol6.min.js',
     format: 'es'
     }
  ],
  plugins: [
    node(),
    cjs(),
    production && terser()
  ],
  onwarn: function(warning, superOnWarn) {
    /*
     * skip certain warnings
     * https://github.com/openlayers/openlayers/issues/10245
     */
    if (warning.code === 'THIS_IS_UNDEFINED') {
      return;
    }
    superOnWarn(warning);
  }
};

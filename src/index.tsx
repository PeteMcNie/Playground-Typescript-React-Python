import * as React from 'react'
import * as ReactDOM from 'react-dom'

import App from './components/App'
import HelloExample from './components/HelloExample'

ReactDOM.render(
  // <App userName="Developer" lang="TypeScript" />,
  // document.getElementById('root'),
  <HelloExample name='Pablo' enthusiasmLevel={6} />,
  document.getElementById('root')
)

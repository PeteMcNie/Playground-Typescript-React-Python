import * as React from 'react'
import * as ReactDOM from 'react-dom'

import { createStore } from 'redux'
import { enthusiasm } from './reducers/index'
import { StoreState } from './types/index'
import { Provider } from 'react-redux'

// import App from './components/App'
import Hello from './containers/Hello'

const store = createStore<StoreState>(enthusiasm, {
  enthusiasmLevel: 1,
  languageName: 'Typescript'
})

ReactDOM.render(
  // <App userName="Developer" lang="TypeScript" />,
  // document.getElementById('root'),
  <Provider store={store}>
    <Hello />
  </Provider>,
  document.getElementById('root') as HTMLElement
)

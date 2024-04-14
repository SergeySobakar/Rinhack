import './App.css'
import Aside from './components/aside/Aside'
import {Outlet} from "react-router-dom"

function App() {

  return (
    <div className="main__cover">
      <Aside />
      <Outlet />
    </div>
  )
}

export default App

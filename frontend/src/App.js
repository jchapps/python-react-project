import './App.css';
import axios from 'axios'
import {useState, useEffect} from 'react'

function App() {
  const [users, setUsers] = useState([])
  useEffect(() => {
    axios.get('/api').then(res => setUsers(res.data))
  }, [])

  return users.map((user, index) => {
    return <h1 key={index}>{user.name} {user.age} {user.id}</h1>
  })
}

export default App;

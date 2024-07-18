
function App() {

  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <div className="flex flex-col justify-center items-center border-2 rounded-lg p-4">
        <div>Login</div>
        <div>
          <i class='bx bxs-user-circle'></i>
          <input type="text" placeholder="username" className="outline-none border rounded-lg p-2 mb-1"/>
        </div>
        <div className="">
          <i class='bx bxs-lock'></i>
          <input type="password" placeholder="password" className="outline-none border rounded-lg p-2 mt-1"/>
        </div>
        <div>creat new <a href="/register" >account</a></div>
      </div>
    </div>
  )
}

export default App

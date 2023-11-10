const App = () => {

    return (
        <div>
            <NewPost />
            <Posts />
            <Paginator />
        </div>
    )
}

const NewPost = () => {
    const [state, setState] = React.useState({
        value: 0
    })

    const addNumber = () => {
        
    }

    return (
        <div>
            <h1>NEW POST HOLDER</h1>
            <div>Value = {state.value}</div>
            <button>+</button>
            <button>-</button>
        </div>
    )
}

const Posts = () => {
    return (
        <h1>POSTS HOLDER</h1>
    )
}

const Paginator = () => {
    return (
        <h1>PAGINATOR HOLDER</h1>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))

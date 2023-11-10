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
        setState({
            ...state,
            value: state.value + 1
        })
    }

    const substractNumber = () => {
        setState({
            ...state,
            value: state.value - 1
        })
    }

    return (
        <div>
            <h1>NEW POST HOLDER</h1>
            <div>Value = {state.value}</div>
            <button onClick={addNumber}>+</button>
            <button onClick={substractNumber}>-</button>
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

const App = () => {

    return (
        <div>
            <NewPost />
            <Posts />
            <Paginator />
        </div>
    )
}



const NewPost = (props) => {
    console.log("on new posts", props)

    return (
        <div>
            <h1>NEW POST HOLDER</h1>
            <div>Value = {props.value}</div>
            <button onClick={props.onClick}>+</button>
            <button onClick={props.onClick1}>-</button>
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

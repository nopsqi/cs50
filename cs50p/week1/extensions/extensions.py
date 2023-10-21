match input("File name: ").split(".")[-1]:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "png":
    case "pdf":
    case "
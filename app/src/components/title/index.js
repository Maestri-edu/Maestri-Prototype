import { Text } from "react-native"
import stylesComponent from "../../design-System/components-styles"


const Title = ({title}) => {
    return(
        <Text style={stylesComponent.title}> {title} </Text>
    )
}

export default Title
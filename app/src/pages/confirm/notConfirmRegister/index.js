import { TouchableOpacity, View,Text, Button } from "react-native"
import stylesComponent from "../../../design-System/components-styles"
import BackGround from "../../../components/backgroud"
import Title from "../../../components/title"
import { useNavigation } from "@react-navigation/native"


const NotConfirmRegister = () => {
    const navigation = useNavigation();

    const goBack = ()=>{
        navigation.navigate("Home")
    }

    const sendAgain = () => {
        
    }

    return(
        <View style={stylesComponent.container}>
            <BackGround/>
            <View style={stylesComponent.contentBox}>
                <Title title={"registro não confirmado"}/>
                <Text style={stylesComponent.text}> não recebeu uma menssagem de confirmação ? 
                <Text onPress={sendAgain} style={stylesComponent.link}> clique aqui  </Text>
                  aqui para enviar novamente. Caso não funcionar entre em contato </Text>
                <TouchableOpacity onPress={goBack} style={stylesComponent.button}>
                    <Text style={stylesComponent.buttonText}> voltar </Text>
                </TouchableOpacity>
            </View>
        </View>
    )
}

export default NotConfirmRegister
import React from "react";
import { View, ImageBackground } from "react-native";
import imageBackground from "../../../assets/backgroundImage.jpg";
import styles from "./styles";

const BackGround = () => {
  return (
    <View style={styles.container}>
      <ImageBackground
        source={imageBackground}
        style={styles.image}
      >
        <View style={styles.mask} />
      </ImageBackground>
    </View>
  );
};

export default BackGround;

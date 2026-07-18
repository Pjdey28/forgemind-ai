import User from "../models/User.model.js";

const generateTokens = async (id) => {
  // return jwt.sign(
  //   { id },
  //   process.env.ACCESS_TOKEN_SECRET,
  //   { expiresIn: process.env.ACCESS_TOKEN_EXPIRY }
  // );

  try {
    const user = await User.findById(id);
    if (!user) {
      throw new Error("User not found");
    }
    const accessToken = user.generateAccessToken();
    const refreshToken = user.generateRefreshToken();

    user.refreshToken = refreshToken;

    await user.save({validateBeforeSave: false});

    return {accessToken, refreshToken}

  } catch (error) {
     console.log("Error in generateTokens:", error);
     throw error;
  }
};

export default generateTokens;
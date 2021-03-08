#include <jni.h>
#include <string>
#include "mylibrary/mylibrary.h"

extern "C" JNIEXPORT jstring JNICALL
Java_com_arcsoft_myapplication_MainActivity_stringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
//    std::string hello = "Hello from C++";
//    return env->NewStringUTF(hello.c_str());
    const std::string stringFromMyLibrary=my_api();
    return env->NewStringUTF(stringFromMyLibrary.c_str());
}
; ModuleID = 'demo.bc'
source_filename = "code_sources/demo.cc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%"class.std::ios_base::Init" = type { i8 }
%struct.option = type { i8*, i32, i32*, i32 }
%"class.std::__cxx11::basic_string" = type { %"struct.std::__cxx11::basic_string<char>::_Alloc_hider", i64, %union.anon }
%"struct.std::__cxx11::basic_string<char>::_Alloc_hider" = type { i8* }
%union.anon = type { i64, [8 x i8] }
%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque
%"class.std::allocator" = type { i8 }

@_ZStL8__ioinit = internal global %"class.std::ios_base::Init" zeroinitializer, align 1, !dbg !0
@__dso_handle = external hidden global i8
@_ZZ4mainE12long_options = internal global [1 x %struct.option] [%struct.option { i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i32 0, i32 0), i32 1, i32* null, i32 102 }], align 16, !dbg !28
@.str = private unnamed_addr constant [5 x i8] c"file\00", align 1
@.str.1 = private unnamed_addr constant [3 x i8] c"f:\00", align 1
@optarg = external dso_local global i8*, align 8
@.str.2 = private unnamed_addr constant [18 x i8] c"Error Parameters!\00", align 1
@.str.3 = private unnamed_addr constant [2 x i8] c"r\00", align 1
@.str.4 = private unnamed_addr constant [21 x i8] c"The quick brown fox \00", align 1
@.str.5 = private unnamed_addr constant [12 x i8] c"jumps over \00", align 1
@.str.6 = private unnamed_addr constant [14 x i8] c"the lazy dog.\00", align 1
@.str.7 = private unnamed_addr constant [27 x i8] c"Though first str/mem Cmp.\0A\00", align 1
@.str.8 = private unnamed_addr constant [4 x i8] c"%s\0A\00", align 1
@.str.9 = private unnamed_addr constant [33 x i8] c"Puzzle solved, Congratulations!\0A\00", align 1
@.str.10 = private unnamed_addr constant [4 x i8] c"123\00", align 1
@llvm.global_ctors = appending global [1 x { i32, void ()*, i8* }] [{ i32, void ()*, i8* } { i32 65535, void ()* @_GLOBAL__sub_I_demo.cc, i8* null }]

; Function Attrs: noinline uwtable
define internal void @__cxx_global_var_init() #0 section ".text.startup" !dbg !1058 {
  call void @_ZNSt8ios_base4InitC1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1) @_ZStL8__ioinit), !dbg !1059
  %1 = call i32 @__cxa_atexit(void (i8*)* bitcast (void (%"class.std::ios_base::Init"*)* @_ZNSt8ios_base4InitD1Ev to void (i8*)*), i8* getelementptr inbounds (%"class.std::ios_base::Init", %"class.std::ios_base::Init"* @_ZStL8__ioinit, i32 0, i32 0), i8* @__dso_handle) #3, !dbg !1061
  ret void, !dbg !1059
}

declare dso_local void @_ZNSt8ios_base4InitC1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1)) unnamed_addr #1

; Function Attrs: nounwind
declare dso_local void @_ZNSt8ios_base4InitD1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1)) unnamed_addr #2

; Function Attrs: nounwind
declare dso_local i32 @__cxa_atexit(void (i8*)*, i8*, i8*) #3

; Function Attrs: noinline nounwind optnone uwtable mustprogress
define dso_local void @_Z3bugv() #4 !dbg !1062 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  call void @llvm.dbg.declare(metadata i32* %1, metadata !1063, metadata !DIExpression()), !dbg !1064
  store i32 0, i32* %1, align 4, !dbg !1064
  call void @llvm.dbg.declare(metadata i32* %2, metadata !1065, metadata !DIExpression()), !dbg !1066
  store i32 10, i32* %2, align 4, !dbg !1066
  call void @llvm.dbg.declare(metadata i32* %3, metadata !1067, metadata !DIExpression()), !dbg !1068
  %4 = load i32, i32* %2, align 4, !dbg !1069
  %5 = load i32, i32* %1, align 4, !dbg !1070
  %6 = sdiv i32 %4, %5, !dbg !1071
  store i32 %6, i32* %3, align 4, !dbg !1072
  ret void, !dbg !1073
}

; Function Attrs: nofree nosync nounwind readnone speculatable willreturn
declare void @llvm.dbg.declare(metadata, metadata, metadata) #5

; Function Attrs: noinline nounwind optnone uwtable mustprogress
define dso_local void @_Z3bugi(i32 %0) #4 !dbg !1074 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  call void @llvm.dbg.declare(metadata i32* %2, metadata !1075, metadata !DIExpression()), !dbg !1076
  call void @llvm.dbg.declare(metadata i32* %3, metadata !1077, metadata !DIExpression()), !dbg !1078
  store i32 0, i32* %3, align 4, !dbg !1078
  call void @llvm.dbg.declare(metadata i32* %4, metadata !1079, metadata !DIExpression()), !dbg !1080
  store i32 10, i32* %4, align 4, !dbg !1080
  call void @llvm.dbg.declare(metadata i32* %5, metadata !1081, metadata !DIExpression()), !dbg !1082
  %6 = load i32, i32* %4, align 4, !dbg !1083
  %7 = load i32, i32* %3, align 4, !dbg !1084
  %8 = sdiv i32 %6, %7, !dbg !1085
  store i32 %8, i32* %5, align 4, !dbg !1086
  ret void, !dbg !1087
}

; Function Attrs: noinline nounwind optnone uwtable mustprogress
define dso_local void @_Z3bugNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE(%"class.std::__cxx11::basic_string"* %0) #4 !dbg !1088 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  call void @llvm.dbg.declare(metadata %"class.std::__cxx11::basic_string"* %0, metadata !1096, metadata !DIExpression()), !dbg !1097
  call void @llvm.dbg.declare(metadata i32* %2, metadata !1098, metadata !DIExpression()), !dbg !1099
  store i32 0, i32* %2, align 4, !dbg !1099
  call void @llvm.dbg.declare(metadata i32* %3, metadata !1100, metadata !DIExpression()), !dbg !1101
  store i32 10, i32* %3, align 4, !dbg !1101
  call void @llvm.dbg.declare(metadata i32* %4, metadata !1102, metadata !DIExpression()), !dbg !1103
  %5 = load i32, i32* %3, align 4, !dbg !1104
  %6 = load i32, i32* %2, align 4, !dbg !1105
  %7 = sdiv i32 %5, %6, !dbg !1106
  store i32 %7, i32* %4, align 4, !dbg !1107
  ret void, !dbg !1108
}

; Function Attrs: noinline norecurse optnone uwtable mustprogress
define dso_local i32 @main(i32 %0, i8** %1) #6 personality i8* bitcast (i32 (...)* @__gxx_personality_v0 to i8*) !dbg !30 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i8**, align 8
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i8*, align 8
  %9 = alloca [201 x i8], align 16
  %10 = alloca %struct._IO_FILE*, align 8
  %11 = alloca [45 x i8], align 16
  %12 = alloca [201 x i8], align 16
  %13 = alloca [201 x i8], align 16
  %14 = alloca [201 x i8], align 16
  %15 = alloca i32, align 4
  %16 = alloca i32, align 4
  %17 = alloca i32, align 4
  %18 = alloca i64, align 8
  %19 = alloca i32, align 4
  %20 = alloca i16, align 2
  %21 = alloca %"class.std::__cxx11::basic_string", align 8
  %22 = alloca %"class.std::allocator", align 1
  %23 = alloca i8*, align 8
  %24 = alloca i32, align 4
  store i32 0, i32* %3, align 4
  store i32 %0, i32* %4, align 4
  call void @llvm.dbg.declare(metadata i32* %4, metadata !1109, metadata !DIExpression()), !dbg !1110
  store i8** %1, i8*** %5, align 8
  call void @llvm.dbg.declare(metadata i8*** %5, metadata !1111, metadata !DIExpression()), !dbg !1112
  call void @llvm.dbg.declare(metadata i32* %6, metadata !1113, metadata !DIExpression()), !dbg !1114
  call void @llvm.dbg.declare(metadata i32* %7, metadata !1115, metadata !DIExpression()), !dbg !1116
  call void @llvm.dbg.declare(metadata i8** %8, metadata !1117, metadata !DIExpression()), !dbg !1118
  br label %25, !dbg !1119

25:                                               ; preds = %36, %2
  %26 = load i32, i32* %4, align 4, !dbg !1120
  %27 = load i8**, i8*** %5, align 8, !dbg !1121
  %28 = call i32 @getopt_long(i32 %26, i8** %27, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i64 0, i64 0), %struct.option* getelementptr inbounds ([1 x %struct.option], [1 x %struct.option]* @_ZZ4mainE12long_options, i64 0, i64 0), i32* %7) #3, !dbg !1122
  store i32 %28, i32* %6, align 4, !dbg !1123
  %29 = icmp ne i32 %28, -1, !dbg !1124
  br i1 %29, label %30, label %37, !dbg !1119

30:                                               ; preds = %25
  %31 = load i32, i32* %6, align 4, !dbg !1125
  switch i32 %31, label %34 [
    i32 102, label %32
  ], !dbg !1127

32:                                               ; preds = %30
  %33 = load i8*, i8** @optarg, align 8, !dbg !1128
  store i8* %33, i8** %8, align 8, !dbg !1130
  br label %36, !dbg !1131

34:                                               ; preds = %30
  %35 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([18 x i8], [18 x i8]* @.str.2, i64 0, i64 0)), !dbg !1132
  br label %36, !dbg !1133

36:                                               ; preds = %34, %32
  br label %25, !dbg !1119, !llvm.loop !1134

37:                                               ; preds = %25
  call void @llvm.dbg.declare(metadata [201 x i8]* %9, metadata !1137, metadata !DIExpression()), !dbg !1141
  call void @llvm.dbg.declare(metadata %struct._IO_FILE** %10, metadata !1142, metadata !DIExpression()), !dbg !1143
  %38 = load i8*, i8** %8, align 8, !dbg !1144
  %39 = call %struct._IO_FILE* @fopen(i8* %38, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.3, i64 0, i64 0)), !dbg !1145
  store %struct._IO_FILE* %39, %struct._IO_FILE** %10, align 8, !dbg !1143
  %40 = getelementptr inbounds [201 x i8], [201 x i8]* %9, i64 0, i64 0, !dbg !1146
  %41 = load %struct._IO_FILE*, %struct._IO_FILE** %10, align 8, !dbg !1147
  %42 = call i8* @fgets(i8* %40, i32 201, %struct._IO_FILE* %41), !dbg !1148
  call void @llvm.dbg.declare(metadata [45 x i8]* %11, metadata !1149, metadata !DIExpression()), !dbg !1153
  %43 = bitcast [45 x i8]* %11 to i8*, !dbg !1153
  call void @llvm.memset.p0i8.i64(i8* align 16 %43, i8 0, i64 45, i1 false), !dbg !1153
  %44 = getelementptr inbounds [45 x i8], [45 x i8]* %11, i64 0, i64 0, !dbg !1154
  %45 = getelementptr inbounds [201 x i8], [201 x i8]* %9, i64 0, i64 0, !dbg !1154
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 16 %44, i8* align 16 %45, i64 44, i1 false), !dbg !1154
  %46 = getelementptr inbounds [45 x i8], [45 x i8]* %11, i64 0, i64 44, !dbg !1155
  store i8 0, i8* %46, align 4, !dbg !1156
  %47 = getelementptr inbounds [45 x i8], [45 x i8]* %11, i64 0, i64 0, !dbg !1157
  %48 = call i32 @memcmp(i8* %47, i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.str.4, i64 0, i64 0), i64 20) #10, !dbg !1159
  %49 = icmp ne i32 %48, 0, !dbg !1160
  br i1 %49, label %58, label %50, !dbg !1161

50:                                               ; preds = %37
  %51 = getelementptr inbounds [45 x i8], [45 x i8]* %11, i64 0, i64 20, !dbg !1162
  %52 = call i32 @strncmp(i8* %51, i8* getelementptr inbounds ([12 x i8], [12 x i8]* @.str.5, i64 0, i64 0), i64 11) #10, !dbg !1163
  %53 = icmp ne i32 %52, 0, !dbg !1164
  br i1 %53, label %58, label %54, !dbg !1165

54:                                               ; preds = %50
  %55 = getelementptr inbounds [45 x i8], [45 x i8]* %11, i64 0, i64 31, !dbg !1166
  %56 = call i32 @strcmp(i8* %55, i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.6, i64 0, i64 0)) #10, !dbg !1167
  %57 = icmp ne i32 %56, 0, !dbg !1168
  br i1 %57, label %58, label %59, !dbg !1169

58:                                               ; preds = %54, %50, %37
  store i32 1, i32* %3, align 4, !dbg !1170
  br label %146, !dbg !1170

59:                                               ; preds = %54
  %60 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([27 x i8], [27 x i8]* @.str.7, i64 0, i64 0)), !dbg !1172
  call void @llvm.dbg.declare(metadata [201 x i8]* %12, metadata !1173, metadata !DIExpression()), !dbg !1174
  call void @llvm.dbg.declare(metadata [201 x i8]* %13, metadata !1175, metadata !DIExpression()), !dbg !1176
  call void @llvm.dbg.declare(metadata [201 x i8]* %14, metadata !1177, metadata !DIExpression()), !dbg !1178
  call void @llvm.dbg.declare(metadata i32* %15, metadata !1179, metadata !DIExpression()), !dbg !1181
  store i32 0, i32* %15, align 4, !dbg !1181
  br label %61, !dbg !1182

61:                                               ; preds = %73, %59
  %62 = load i32, i32* %15, align 4, !dbg !1183
  %63 = icmp slt i32 %62, 16, !dbg !1185
  br i1 %63, label %64, label %76, !dbg !1186

64:                                               ; preds = %61
  %65 = load i32, i32* %15, align 4, !dbg !1187
  %66 = add nsw i32 %65, 44, !dbg !1189
  %67 = sext i32 %66 to i64, !dbg !1190
  %68 = getelementptr inbounds [201 x i8], [201 x i8]* %9, i64 0, i64 %67, !dbg !1190
  %69 = load i8, i8* %68, align 1, !dbg !1190
  %70 = load i32, i32* %15, align 4, !dbg !1191
  %71 = sext i32 %70 to i64, !dbg !1192
  %72 = getelementptr inbounds [201 x i8], [201 x i8]* %12, i64 0, i64 %71, !dbg !1192
  store i8 %69, i8* %72, align 1, !dbg !1193
  br label %73, !dbg !1194

73:                                               ; preds = %64
  %74 = load i32, i32* %15, align 4, !dbg !1195
  %75 = add nsw i32 %74, 1, !dbg !1195
  store i32 %75, i32* %15, align 4, !dbg !1195
  br label %61, !dbg !1196, !llvm.loop !1197

76:                                               ; preds = %61
  %77 = getelementptr inbounds [201 x i8], [201 x i8]* %12, i64 0, i64 16, !dbg !1199
  store i8 0, i8* %77, align 16, !dbg !1200
  call void @llvm.dbg.declare(metadata i32* %16, metadata !1201, metadata !DIExpression()), !dbg !1203
  store i32 0, i32* %16, align 4, !dbg !1203
  br label %78, !dbg !1204

78:                                               ; preds = %91, %76
  %79 = load i32, i32* %16, align 4, !dbg !1205
  %80 = icmp slt i32 %79, 8, !dbg !1207
  br i1 %80, label %81, label %94, !dbg !1208

81:                                               ; preds = %78
  %82 = load i32, i32* %16, align 4, !dbg !1209
  %83 = add nsw i32 %82, 44, !dbg !1211
  %84 = add nsw i32 %83, 16, !dbg !1212
  %85 = sext i32 %84 to i64, !dbg !1213
  %86 = getelementptr inbounds [201 x i8], [201 x i8]* %9, i64 0, i64 %85, !dbg !1213
  %87 = load i8, i8* %86, align 1, !dbg !1213
  %88 = load i32, i32* %16, align 4, !dbg !1214
  %89 = sext i32 %88 to i64, !dbg !1215
  %90 = getelementptr inbounds [201 x i8], [201 x i8]* %13, i64 0, i64 %89, !dbg !1215
  store i8 %87, i8* %90, align 1, !dbg !1216
  br label %91, !dbg !1217

91:                                               ; preds = %81
  %92 = load i32, i32* %16, align 4, !dbg !1218
  %93 = add nsw i32 %92, 1, !dbg !1218
  store i32 %93, i32* %16, align 4, !dbg !1218
  br label %78, !dbg !1219, !llvm.loop !1220

94:                                               ; preds = %78
  %95 = getelementptr inbounds [201 x i8], [201 x i8]* %13, i64 0, i64 8, !dbg !1222
  store i8 0, i8* %95, align 8, !dbg !1223
  call void @llvm.dbg.declare(metadata i32* %17, metadata !1224, metadata !DIExpression()), !dbg !1226
  store i32 0, i32* %17, align 4, !dbg !1226
  br label %96, !dbg !1227

96:                                               ; preds = %110, %94
  %97 = load i32, i32* %17, align 4, !dbg !1228
  %98 = icmp slt i32 %97, 4, !dbg !1230
  br i1 %98, label %99, label %113, !dbg !1231

99:                                               ; preds = %96
  %100 = load i32, i32* %17, align 4, !dbg !1232
  %101 = add nsw i32 %100, 44, !dbg !1234
  %102 = add nsw i32 %101, 16, !dbg !1235
  %103 = add nsw i32 %102, 8, !dbg !1236
  %104 = sext i32 %103 to i64, !dbg !1237
  %105 = getelementptr inbounds [201 x i8], [201 x i8]* %9, i64 0, i64 %104, !dbg !1237
  %106 = load i8, i8* %105, align 1, !dbg !1237
  %107 = load i32, i32* %17, align 4, !dbg !1238
  %108 = sext i32 %107 to i64, !dbg !1239
  %109 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 %108, !dbg !1239
  store i8 %106, i8* %109, align 1, !dbg !1240
  br label %110, !dbg !1241

110:                                              ; preds = %99
  %111 = load i32, i32* %17, align 4, !dbg !1242
  %112 = add nsw i32 %111, 1, !dbg !1242
  store i32 %112, i32* %17, align 4, !dbg !1242
  br label %96, !dbg !1243, !llvm.loop !1244

113:                                              ; preds = %96
  %114 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 4, !dbg !1246
  store i8 0, i8* %114, align 4, !dbg !1247
  %115 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 0, !dbg !1248
  %116 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.8, i64 0, i64 0), i8* %115), !dbg !1249
  call void @llvm.dbg.declare(metadata i64* %18, metadata !1250, metadata !DIExpression()), !dbg !1251
  %117 = getelementptr inbounds [201 x i8], [201 x i8]* %12, i64 0, i64 0, !dbg !1252
  %118 = call i64 @strtoull(i8* %117, i8** null, i32 16) #3, !dbg !1253
  store i64 %118, i64* %18, align 8, !dbg !1251
  %119 = load i64, i64* %18, align 8, !dbg !1254
  %120 = icmp ne i64 %119, -3819410105351357762, !dbg !1256
  br i1 %120, label %121, label %122, !dbg !1257

121:                                              ; preds = %113
  store i32 1, i32* %3, align 4, !dbg !1258
  br label %146, !dbg !1258

122:                                              ; preds = %113
  call void @llvm.dbg.declare(metadata i32* %19, metadata !1260, metadata !DIExpression()), !dbg !1261
  %123 = getelementptr inbounds [201 x i8], [201 x i8]* %13, i64 0, i64 0, !dbg !1262
  %124 = call i64 @strtoul(i8* %123, i8** null, i32 16) #3, !dbg !1263
  %125 = trunc i64 %124 to i32, !dbg !1263
  store i32 %125, i32* %19, align 4, !dbg !1261
  %126 = load i32, i32* %19, align 4, !dbg !1264
  %127 = icmp ne i32 %126, -559038242, !dbg !1266
  br i1 %127, label %128, label %129, !dbg !1267

128:                                              ; preds = %122
  store i32 1, i32* %3, align 4, !dbg !1268
  br label %146, !dbg !1268

129:                                              ; preds = %122
  call void @llvm.dbg.declare(metadata i16* %20, metadata !1270, metadata !DIExpression()), !dbg !1271
  %130 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 0, !dbg !1272
  %131 = call i64 @strtouq(i8* %130, i8** null, i32 16) #3, !dbg !1273
  %132 = trunc i64 %131 to i16, !dbg !1273
  store i16 %132, i16* %20, align 2, !dbg !1271
  %133 = load i16, i16* %20, align 2, !dbg !1274
  %134 = zext i16 %133 to i32, !dbg !1274
  switch i32 %134, label %138 [
    i32 43981, label %135
    i32 61374, label %136
    i32 48879, label %137
  ], !dbg !1275

135:                                              ; preds = %129
  store i32 1, i32* %3, align 4, !dbg !1276
  br label %146, !dbg !1276

136:                                              ; preds = %129
  store i32 1, i32* %3, align 4, !dbg !1278
  br label %146, !dbg !1278

137:                                              ; preds = %129
  br label %139, !dbg !1279

138:                                              ; preds = %129
  store i32 1, i32* %3, align 4, !dbg !1280
  br label %146, !dbg !1280

139:                                              ; preds = %137
  %140 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([33 x i8], [33 x i8]* @.str.9, i64 0, i64 0)), !dbg !1281
  call void @_Z3bugv(), !dbg !1282
  call void @_ZNSaIcEC1Ev(%"class.std::allocator"* nonnull dereferenceable(1) %22) #3, !dbg !1283
  invoke void @_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_(%"class.std::__cxx11::basic_string"* nonnull dereferenceable(32) %21, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.10, i64 0, i64 0), %"class.std::allocator"* nonnull align 1 dereferenceable(1) %22)
          to label %141 unwind label %142, !dbg !1283

141:                                              ; preds = %139
  call void @_Z3bugNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE(%"class.std::__cxx11::basic_string"* %21), !dbg !1284
  call void @_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev(%"class.std::__cxx11::basic_string"* nonnull dereferenceable(32) %21) #3, !dbg !1284
  call void @_ZNSaIcED1Ev(%"class.std::allocator"* nonnull dereferenceable(1) %22) #3, !dbg !1284
  call void @_Z3bugi(i32 123), !dbg !1285
  store i32 0, i32* %3, align 4, !dbg !1286
  br label %146, !dbg !1286

142:                                              ; preds = %139
  %143 = landingpad { i8*, i32 }
          cleanup, !dbg !1287
  %144 = extractvalue { i8*, i32 } %143, 0, !dbg !1287
  store i8* %144, i8** %23, align 8, !dbg !1287
  %145 = extractvalue { i8*, i32 } %143, 1, !dbg !1287
  store i32 %145, i32* %24, align 4, !dbg !1287
  call void @_ZNSaIcED1Ev(%"class.std::allocator"* nonnull dereferenceable(1) %22) #3, !dbg !1284
  br label %148, !dbg !1284

146:                                              ; preds = %141, %138, %136, %135, %128, %121, %58
  %147 = load i32, i32* %3, align 4, !dbg !1287
  ret i32 %147, !dbg !1287

148:                                              ; preds = %142
  %149 = load i8*, i8** %23, align 8, !dbg !1284
  %150 = load i32, i32* %24, align 4, !dbg !1284
  %151 = insertvalue { i8*, i32 } undef, i8* %149, 0, !dbg !1284
  %152 = insertvalue { i8*, i32 } %151, i32 %150, 1, !dbg !1284
  resume { i8*, i32 } %152, !dbg !1284
}

; Function Attrs: nounwind
declare dso_local i32 @getopt_long(i32, i8**, i8*, %struct.option*, i32*) #2

declare dso_local i32 @printf(i8*, ...) #1

declare dso_local %struct._IO_FILE* @fopen(i8*, i8*) #1

declare dso_local i8* @fgets(i8*, i32, %struct._IO_FILE*) #1

; Function Attrs: argmemonly nofree nosync nounwind willreturn writeonly
declare void @llvm.memset.p0i8.i64(i8* nocapture writeonly, i8, i64, i1 immarg) #7

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg) #8

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @memcmp(i8*, i8*, i64) #9

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @strncmp(i8*, i8*, i64) #9

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @strcmp(i8*, i8*) #9

; Function Attrs: nounwind
declare dso_local i64 @strtoull(i8*, i8**, i32) #2

; Function Attrs: nounwind
declare dso_local i64 @strtoul(i8*, i8**, i32) #2

; Function Attrs: nounwind
declare dso_local i64 @strtouq(i8*, i8**, i32) #2

; Function Attrs: nounwind
declare dso_local void @_ZNSaIcEC1Ev(%"class.std::allocator"* nonnull dereferenceable(1)) unnamed_addr #2

declare dso_local void @_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_(%"class.std::__cxx11::basic_string"* nonnull dereferenceable(32), i8*, %"class.std::allocator"* nonnull align 1 dereferenceable(1)) unnamed_addr #1

declare dso_local i32 @__gxx_personality_v0(...)

; Function Attrs: nounwind
declare dso_local void @_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev(%"class.std::__cxx11::basic_string"* nonnull dereferenceable(32)) unnamed_addr #2

; Function Attrs: nounwind
declare dso_local void @_ZNSaIcED1Ev(%"class.std::allocator"* nonnull dereferenceable(1)) unnamed_addr #2

; Function Attrs: noinline uwtable
define internal void @_GLOBAL__sub_I_demo.cc() #0 section ".text.startup" !dbg !1288 {
  call void @__cxx_global_var_init(), !dbg !1290
  ret void
}

attributes #0 = { noinline uwtable "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }
attributes #4 = { noinline nounwind optnone uwtable mustprogress "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #5 = { nofree nosync nounwind readnone speculatable willreturn }
attributes #6 = { noinline norecurse optnone uwtable mustprogress "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #7 = { argmemonly nofree nosync nounwind willreturn writeonly }
attributes #8 = { argmemonly nofree nosync nounwind willreturn }
attributes #9 = { nounwind readonly willreturn "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #10 = { nounwind readonly willreturn }

!llvm.dbg.cu = !{!37}
!llvm.module.flags = !{!1054, !1055, !1056}
!llvm.ident = !{!1057}

!0 = !DIGlobalVariableExpression(var: !1, expr: !DIExpression())
!1 = distinct !DIGlobalVariable(name: "__ioinit", linkageName: "_ZStL8__ioinit", scope: !2, file: !3, line: 74, type: !4, isLocal: true, isDefinition: true)
!2 = !DINamespace(name: "std", scope: null)
!3 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream", directory: "")
!4 = distinct !DICompositeType(tag: DW_TAG_class_type, name: "Init", scope: !6, file: !5, line: 608, size: 8, flags: DIFlagTypePassByReference | DIFlagNonTrivial, elements: !7, identifier: "_ZTSNSt8ios_base4InitE")
!5 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/ios_base.h", directory: "")
!6 = !DICompositeType(tag: DW_TAG_class_type, name: "ios_base", scope: !2, file: !5, line: 228, size: 1728, flags: DIFlagFwdDecl | DIFlagNonTrivial)
!7 = !{!8, !12, !14, !18, !19, !24}
!8 = !DIDerivedType(tag: DW_TAG_member, name: "_S_refcount", scope: !4, file: !5, line: 621, baseType: !9, flags: DIFlagStaticMember)
!9 = !DIDerivedType(tag: DW_TAG_typedef, name: "_Atomic_word", file: !10, line: 32, baseType: !11)
!10 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/x86_64-linux-gnu/c++/9/bits/atomic_word.h", directory: "")
!11 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!12 = !DIDerivedType(tag: DW_TAG_member, name: "_S_synced_with_stdio", scope: !4, file: !5, line: 622, baseType: !13, flags: DIFlagStaticMember)
!13 = !DIBasicType(name: "bool", size: 8, encoding: DW_ATE_boolean)
!14 = !DISubprogram(name: "Init", scope: !4, file: !5, line: 612, type: !15, scopeLine: 612, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!15 = !DISubroutineType(types: !16)
!16 = !{null, !17}
!17 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !4, size: 64, flags: DIFlagArtificial | DIFlagObjectPointer)
!18 = !DISubprogram(name: "~Init", scope: !4, file: !5, line: 613, type: !15, scopeLine: 613, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!19 = !DISubprogram(name: "Init", scope: !4, file: !5, line: 616, type: !20, scopeLine: 616, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!20 = !DISubroutineType(types: !21)
!21 = !{null, !17, !22}
!22 = !DIDerivedType(tag: DW_TAG_reference_type, baseType: !23, size: 64)
!23 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !4)
!24 = !DISubprogram(name: "operator=", linkageName: "_ZNSt8ios_base4InitaSERKS0_", scope: !4, file: !5, line: 617, type: !25, scopeLine: 617, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!25 = !DISubroutineType(types: !26)
!26 = !{!27, !17, !22}
!27 = !DIDerivedType(tag: DW_TAG_reference_type, baseType: !4, size: 64)
!28 = !DIGlobalVariableExpression(var: !29, expr: !DIExpression())
!29 = distinct !DIGlobalVariable(name: "long_options", scope: !30, file: !31, line: 39, type: !1043, isLocal: true, isDefinition: true)
!30 = distinct !DISubprogram(name: "main", scope: !31, file: !31, line: 35, type: !32, scopeLine: 35, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !37, retainedNodes: !38)
!31 = !DIFile(filename: "code_sources/demo.cc", directory: "/home/fzz/Desktop/STFGFuzz/Programs/demo")
!32 = !DISubroutineType(types: !33)
!33 = !{!11, !11, !34}
!34 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !35, size: 64)
!35 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !36, size: 64)
!36 = !DIBasicType(name: "char", size: 8, encoding: DW_ATE_signed_char)
!37 = distinct !DICompileUnit(language: DW_LANG_C_plus_plus_14, file: !31, producer: "clang version 12.0.1 (git@github.com:fengzhengzhan/STFGFuzz.git 4ed35f2f97b6ad76c9de46553c4fdd545c0c1eb2)", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !38, globals: !39, imports: !40, splitDebugInlining: false, nameTableKind: None)
!38 = !{}
!39 = !{!0, !28}
!40 = !{!41, !48, !52, !55, !59, !62, !64, !66, !68, !71, !74, !77, !80, !83, !85, !90, !94, !98, !102, !104, !106, !108, !110, !113, !116, !119, !122, !125, !127, !133, !139, !144, !148, !150, !152, !154, !156, !163, !168, !175, !179, !183, !187, !195, !199, !201, !205, !211, !215, !222, !224, !228, !232, !236, !238, !242, !246, !248, !252, !254, !256, !260, !264, !268, !272, !276, !280, !282, !293, !297, !301, !306, !308, !310, !314, !318, !319, !320, !321, !322, !323, !327, !331, !337, !341, !346, !348, !353, !355, !359, !367, !371, !375, !379, !383, !387, !391, !395, !399, !403, !410, !414, !418, !420, !422, !426, !430, !435, !439, !443, !445, !452, !456, !463, !465, !469, !473, !477, !481, !486, !491, !496, !497, !498, !499, !501, !502, !503, !504, !505, !506, !507, !513, !517, !521, !525, !529, !533, !535, !537, !539, !543, !547, !551, !555, !559, !561, !563, !565, !569, !573, !577, !579, !581, !598, !601, !606, !613, !618, !622, !626, !630, !634, !636, !638, !642, !648, !652, !658, !664, !666, !670, !674, !678, !682, !686, !688, !692, !696, !700, !702, !706, !710, !714, !716, !718, !722, !730, !734, !738, !742, !744, !750, !752, !758, !762, !766, !770, !774, !778, !782, !784, !786, !790, !794, !798, !800, !804, !808, !810, !812, !816, !820, !824, !828, !829, !830, !831, !832, !833, !834, !835, !836, !837, !838, !893, !897, !901, !905, !909, !914, !918, !920, !922, !924, !926, !928, !930, !932, !934, !936, !938, !940, !942, !944, !947, !949, !955, !958, !959, !961, !963, !965, !967, !971, !973, !975, !977, !979, !981, !983, !985, !987, !991, !995, !997, !1001, !1005, !1007, !1008, !1009, !1010, !1011, !1012, !1013, !1018, !1019, !1020, !1021, !1022, !1023, !1024, !1025, !1026, !1027, !1028, !1029, !1030, !1031, !1032, !1033, !1034, !1035, !1036, !1037, !1038, !1039, !1040, !1041, !1042}
!41 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !42, file: !47, line: 47)
!42 = !DIDerivedType(tag: DW_TAG_typedef, name: "int8_t", file: !43, line: 24, baseType: !44)
!43 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/stdint-intn.h", directory: "")
!44 = !DIDerivedType(tag: DW_TAG_typedef, name: "__int8_t", file: !45, line: 37, baseType: !46)
!45 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/types.h", directory: "")
!46 = !DIBasicType(name: "signed char", size: 8, encoding: DW_ATE_signed_char)
!47 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/cstdint", directory: "")
!48 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !49, file: !47, line: 48)
!49 = !DIDerivedType(tag: DW_TAG_typedef, name: "int16_t", file: !43, line: 25, baseType: !50)
!50 = !DIDerivedType(tag: DW_TAG_typedef, name: "__int16_t", file: !45, line: 39, baseType: !51)
!51 = !DIBasicType(name: "short", size: 16, encoding: DW_ATE_signed)
!52 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !53, file: !47, line: 49)
!53 = !DIDerivedType(tag: DW_TAG_typedef, name: "int32_t", file: !43, line: 26, baseType: !54)
!54 = !DIDerivedType(tag: DW_TAG_typedef, name: "__int32_t", file: !45, line: 41, baseType: !11)
!55 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !56, file: !47, line: 50)
!56 = !DIDerivedType(tag: DW_TAG_typedef, name: "int64_t", file: !43, line: 27, baseType: !57)
!57 = !DIDerivedType(tag: DW_TAG_typedef, name: "__int64_t", file: !45, line: 44, baseType: !58)
!58 = !DIBasicType(name: "long int", size: 64, encoding: DW_ATE_signed)
!59 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !60, file: !47, line: 52)
!60 = !DIDerivedType(tag: DW_TAG_typedef, name: "int_fast8_t", file: !61, line: 58, baseType: !46)
!61 = !DIFile(filename: "/usr/include/stdint.h", directory: "")
!62 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !63, file: !47, line: 53)
!63 = !DIDerivedType(tag: DW_TAG_typedef, name: "int_fast16_t", file: !61, line: 60, baseType: !58)
!64 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !65, file: !47, line: 54)
!65 = !DIDerivedType(tag: DW_TAG_typedef, name: "int_fast32_t", file: !61, line: 61, baseType: !58)
!66 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !67, file: !47, line: 55)
!67 = !DIDerivedType(tag: DW_TAG_typedef, name: "int_fast64_t", file: !61, line: 62, baseType: !58)
!68 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !69, file: !47, line: 57)
!69 = !DIDerivedType(tag: DW_TAG_typedef, name: "int_least8_t", file: !61, line: 43, baseType: !70)
!70 = !DIDerivedType(tag: DW_TAG_typedef, name: "__int_least8_t", file: !45, line: 52, baseType: !44)
!71 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !72, file: !47, line: 58)
!72 = !DIDerivedType(tag: DW_TAG_typedef, name: "int_least16_t", file: !61, line: 44, baseType: !73)
!73 = !DIDerivedType(tag: DW_TAG_typedef, name: "__int_least16_t", file: !45, line: 54, baseType: !50)
!74 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !75, file: !47, line: 59)
!75 = !DIDerivedType(tag: DW_TAG_typedef, name: "int_least32_t", file: !61, line: 45, baseType: !76)
!76 = !DIDerivedType(tag: DW_TAG_typedef, name: "__int_least32_t", file: !45, line: 56, baseType: !54)
!77 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !78, file: !47, line: 60)
!78 = !DIDerivedType(tag: DW_TAG_typedef, name: "int_least64_t", file: !61, line: 46, baseType: !79)
!79 = !DIDerivedType(tag: DW_TAG_typedef, name: "__int_least64_t", file: !45, line: 58, baseType: !57)
!80 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !81, file: !47, line: 62)
!81 = !DIDerivedType(tag: DW_TAG_typedef, name: "intmax_t", file: !61, line: 101, baseType: !82)
!82 = !DIDerivedType(tag: DW_TAG_typedef, name: "__intmax_t", file: !45, line: 72, baseType: !58)
!83 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !84, file: !47, line: 63)
!84 = !DIDerivedType(tag: DW_TAG_typedef, name: "intptr_t", file: !61, line: 87, baseType: !58)
!85 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !86, file: !47, line: 65)
!86 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint8_t", file: !87, line: 24, baseType: !88)
!87 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/stdint-uintn.h", directory: "")
!88 = !DIDerivedType(tag: DW_TAG_typedef, name: "__uint8_t", file: !45, line: 38, baseType: !89)
!89 = !DIBasicType(name: "unsigned char", size: 8, encoding: DW_ATE_unsigned_char)
!90 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !91, file: !47, line: 66)
!91 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint16_t", file: !87, line: 25, baseType: !92)
!92 = !DIDerivedType(tag: DW_TAG_typedef, name: "__uint16_t", file: !45, line: 40, baseType: !93)
!93 = !DIBasicType(name: "unsigned short", size: 16, encoding: DW_ATE_unsigned)
!94 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !95, file: !47, line: 67)
!95 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint32_t", file: !87, line: 26, baseType: !96)
!96 = !DIDerivedType(tag: DW_TAG_typedef, name: "__uint32_t", file: !45, line: 42, baseType: !97)
!97 = !DIBasicType(name: "unsigned int", size: 32, encoding: DW_ATE_unsigned)
!98 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !99, file: !47, line: 68)
!99 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint64_t", file: !87, line: 27, baseType: !100)
!100 = !DIDerivedType(tag: DW_TAG_typedef, name: "__uint64_t", file: !45, line: 45, baseType: !101)
!101 = !DIBasicType(name: "long unsigned int", size: 64, encoding: DW_ATE_unsigned)
!102 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !103, file: !47, line: 70)
!103 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint_fast8_t", file: !61, line: 71, baseType: !89)
!104 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !105, file: !47, line: 71)
!105 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint_fast16_t", file: !61, line: 73, baseType: !101)
!106 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !107, file: !47, line: 72)
!107 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint_fast32_t", file: !61, line: 74, baseType: !101)
!108 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !109, file: !47, line: 73)
!109 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint_fast64_t", file: !61, line: 75, baseType: !101)
!110 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !111, file: !47, line: 75)
!111 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint_least8_t", file: !61, line: 49, baseType: !112)
!112 = !DIDerivedType(tag: DW_TAG_typedef, name: "__uint_least8_t", file: !45, line: 53, baseType: !88)
!113 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !114, file: !47, line: 76)
!114 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint_least16_t", file: !61, line: 50, baseType: !115)
!115 = !DIDerivedType(tag: DW_TAG_typedef, name: "__uint_least16_t", file: !45, line: 55, baseType: !92)
!116 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !117, file: !47, line: 77)
!117 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint_least32_t", file: !61, line: 51, baseType: !118)
!118 = !DIDerivedType(tag: DW_TAG_typedef, name: "__uint_least32_t", file: !45, line: 57, baseType: !96)
!119 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !120, file: !47, line: 78)
!120 = !DIDerivedType(tag: DW_TAG_typedef, name: "uint_least64_t", file: !61, line: 52, baseType: !121)
!121 = !DIDerivedType(tag: DW_TAG_typedef, name: "__uint_least64_t", file: !45, line: 59, baseType: !100)
!122 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !123, file: !47, line: 80)
!123 = !DIDerivedType(tag: DW_TAG_typedef, name: "uintmax_t", file: !61, line: 102, baseType: !124)
!124 = !DIDerivedType(tag: DW_TAG_typedef, name: "__uintmax_t", file: !45, line: 73, baseType: !101)
!125 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !126, file: !47, line: 81)
!126 = !DIDerivedType(tag: DW_TAG_typedef, name: "uintptr_t", file: !61, line: 90, baseType: !101)
!127 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !128, file: !132, line: 98)
!128 = !DIDerivedType(tag: DW_TAG_typedef, name: "FILE", file: !129, line: 7, baseType: !130)
!129 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/types/FILE.h", directory: "")
!130 = !DICompositeType(tag: DW_TAG_structure_type, name: "_IO_FILE", file: !131, line: 49, size: 1728, flags: DIFlagFwdDecl, identifier: "_ZTS8_IO_FILE")
!131 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h", directory: "")
!132 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/cstdio", directory: "")
!133 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !134, file: !132, line: 99)
!134 = !DIDerivedType(tag: DW_TAG_typedef, name: "fpos_t", file: !135, line: 84, baseType: !136)
!135 = !DIFile(filename: "/usr/include/stdio.h", directory: "")
!136 = !DIDerivedType(tag: DW_TAG_typedef, name: "__fpos_t", file: !137, line: 14, baseType: !138)
!137 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/types/__fpos_t.h", directory: "")
!138 = !DICompositeType(tag: DW_TAG_structure_type, name: "_G_fpos_t", file: !137, line: 10, size: 128, flags: DIFlagFwdDecl, identifier: "_ZTS9_G_fpos_t")
!139 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !140, file: !132, line: 101)
!140 = !DISubprogram(name: "clearerr", scope: !135, file: !135, line: 757, type: !141, flags: DIFlagPrototyped, spFlags: 0)
!141 = !DISubroutineType(types: !142)
!142 = !{null, !143}
!143 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !128, size: 64)
!144 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !145, file: !132, line: 102)
!145 = !DISubprogram(name: "fclose", scope: !135, file: !135, line: 213, type: !146, flags: DIFlagPrototyped, spFlags: 0)
!146 = !DISubroutineType(types: !147)
!147 = !{!11, !143}
!148 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !149, file: !132, line: 103)
!149 = !DISubprogram(name: "feof", scope: !135, file: !135, line: 759, type: !146, flags: DIFlagPrototyped, spFlags: 0)
!150 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !151, file: !132, line: 104)
!151 = !DISubprogram(name: "ferror", scope: !135, file: !135, line: 761, type: !146, flags: DIFlagPrototyped, spFlags: 0)
!152 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !153, file: !132, line: 105)
!153 = !DISubprogram(name: "fflush", scope: !135, file: !135, line: 218, type: !146, flags: DIFlagPrototyped, spFlags: 0)
!154 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !155, file: !132, line: 106)
!155 = !DISubprogram(name: "fgetc", scope: !135, file: !135, line: 485, type: !146, flags: DIFlagPrototyped, spFlags: 0)
!156 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !157, file: !132, line: 107)
!157 = !DISubprogram(name: "fgetpos", scope: !135, file: !135, line: 731, type: !158, flags: DIFlagPrototyped, spFlags: 0)
!158 = !DISubroutineType(types: !159)
!159 = !{!11, !160, !161}
!160 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !143)
!161 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !162)
!162 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !134, size: 64)
!163 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !164, file: !132, line: 108)
!164 = !DISubprogram(name: "fgets", scope: !135, file: !135, line: 564, type: !165, flags: DIFlagPrototyped, spFlags: 0)
!165 = !DISubroutineType(types: !166)
!166 = !{!35, !167, !11, !160}
!167 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !35)
!168 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !169, file: !132, line: 109)
!169 = !DISubprogram(name: "fopen", scope: !135, file: !135, line: 246, type: !170, flags: DIFlagPrototyped, spFlags: 0)
!170 = !DISubroutineType(types: !171)
!171 = !{!143, !172, !172}
!172 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !173)
!173 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !174, size: 64)
!174 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !36)
!175 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !176, file: !132, line: 110)
!176 = !DISubprogram(name: "fprintf", scope: !135, file: !135, line: 326, type: !177, flags: DIFlagPrototyped, spFlags: 0)
!177 = !DISubroutineType(types: !178)
!178 = !{!11, !160, !172, null}
!179 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !180, file: !132, line: 111)
!180 = !DISubprogram(name: "fputc", scope: !135, file: !135, line: 521, type: !181, flags: DIFlagPrototyped, spFlags: 0)
!181 = !DISubroutineType(types: !182)
!182 = !{!11, !11, !143}
!183 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !184, file: !132, line: 112)
!184 = !DISubprogram(name: "fputs", scope: !135, file: !135, line: 626, type: !185, flags: DIFlagPrototyped, spFlags: 0)
!185 = !DISubroutineType(types: !186)
!186 = !{!11, !172, !160}
!187 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !188, file: !132, line: 113)
!188 = !DISubprogram(name: "fread", scope: !135, file: !135, line: 646, type: !189, flags: DIFlagPrototyped, spFlags: 0)
!189 = !DISubroutineType(types: !190)
!190 = !{!191, !193, !191, !191, !160}
!191 = !DIDerivedType(tag: DW_TAG_typedef, name: "size_t", file: !192, line: 46, baseType: !101)
!192 = !DIFile(filename: "/usr/local/lib/clang/12.0.1/include/stddef.h", directory: "")
!193 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !194)
!194 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: null, size: 64)
!195 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !196, file: !132, line: 114)
!196 = !DISubprogram(name: "freopen", scope: !135, file: !135, line: 252, type: !197, flags: DIFlagPrototyped, spFlags: 0)
!197 = !DISubroutineType(types: !198)
!198 = !{!143, !172, !172, !160}
!199 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !200, file: !132, line: 115)
!200 = !DISubprogram(name: "fscanf", linkageName: "__isoc99_fscanf", scope: !135, file: !135, line: 407, type: !177, flags: DIFlagPrototyped, spFlags: 0)
!201 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !202, file: !132, line: 116)
!202 = !DISubprogram(name: "fseek", scope: !135, file: !135, line: 684, type: !203, flags: DIFlagPrototyped, spFlags: 0)
!203 = !DISubroutineType(types: !204)
!204 = !{!11, !143, !58, !11}
!205 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !206, file: !132, line: 117)
!206 = !DISubprogram(name: "fsetpos", scope: !135, file: !135, line: 736, type: !207, flags: DIFlagPrototyped, spFlags: 0)
!207 = !DISubroutineType(types: !208)
!208 = !{!11, !143, !209}
!209 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !210, size: 64)
!210 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !134)
!211 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !212, file: !132, line: 118)
!212 = !DISubprogram(name: "ftell", scope: !135, file: !135, line: 689, type: !213, flags: DIFlagPrototyped, spFlags: 0)
!213 = !DISubroutineType(types: !214)
!214 = !{!58, !143}
!215 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !216, file: !132, line: 119)
!216 = !DISubprogram(name: "fwrite", scope: !135, file: !135, line: 652, type: !217, flags: DIFlagPrototyped, spFlags: 0)
!217 = !DISubroutineType(types: !218)
!218 = !{!191, !219, !191, !191, !160}
!219 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !220)
!220 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !221, size: 64)
!221 = !DIDerivedType(tag: DW_TAG_const_type, baseType: null)
!222 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !223, file: !132, line: 120)
!223 = !DISubprogram(name: "getc", scope: !135, file: !135, line: 486, type: !146, flags: DIFlagPrototyped, spFlags: 0)
!224 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !225, file: !132, line: 121)
!225 = !DISubprogram(name: "getchar", scope: !135, file: !135, line: 492, type: !226, flags: DIFlagPrototyped, spFlags: 0)
!226 = !DISubroutineType(types: !227)
!227 = !{!11}
!228 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !229, file: !132, line: 126)
!229 = !DISubprogram(name: "perror", scope: !135, file: !135, line: 775, type: !230, flags: DIFlagPrototyped, spFlags: 0)
!230 = !DISubroutineType(types: !231)
!231 = !{null, !173}
!232 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !233, file: !132, line: 127)
!233 = !DISubprogram(name: "printf", scope: !135, file: !135, line: 332, type: !234, flags: DIFlagPrototyped, spFlags: 0)
!234 = !DISubroutineType(types: !235)
!235 = !{!11, !172, null}
!236 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !237, file: !132, line: 128)
!237 = !DISubprogram(name: "putc", scope: !135, file: !135, line: 522, type: !181, flags: DIFlagPrototyped, spFlags: 0)
!238 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !239, file: !132, line: 129)
!239 = !DISubprogram(name: "putchar", scope: !135, file: !135, line: 528, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!240 = !DISubroutineType(types: !241)
!241 = !{!11, !11}
!242 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !243, file: !132, line: 130)
!243 = !DISubprogram(name: "puts", scope: !135, file: !135, line: 632, type: !244, flags: DIFlagPrototyped, spFlags: 0)
!244 = !DISubroutineType(types: !245)
!245 = !{!11, !173}
!246 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !247, file: !132, line: 131)
!247 = !DISubprogram(name: "remove", scope: !135, file: !135, line: 146, type: !244, flags: DIFlagPrototyped, spFlags: 0)
!248 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !249, file: !132, line: 132)
!249 = !DISubprogram(name: "rename", scope: !135, file: !135, line: 148, type: !250, flags: DIFlagPrototyped, spFlags: 0)
!250 = !DISubroutineType(types: !251)
!251 = !{!11, !173, !173}
!252 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !253, file: !132, line: 133)
!253 = !DISubprogram(name: "rewind", scope: !135, file: !135, line: 694, type: !141, flags: DIFlagPrototyped, spFlags: 0)
!254 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !255, file: !132, line: 134)
!255 = !DISubprogram(name: "scanf", linkageName: "__isoc99_scanf", scope: !135, file: !135, line: 410, type: !234, flags: DIFlagPrototyped, spFlags: 0)
!256 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !257, file: !132, line: 135)
!257 = !DISubprogram(name: "setbuf", scope: !135, file: !135, line: 304, type: !258, flags: DIFlagPrototyped, spFlags: 0)
!258 = !DISubroutineType(types: !259)
!259 = !{null, !160, !167}
!260 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !261, file: !132, line: 136)
!261 = !DISubprogram(name: "setvbuf", scope: !135, file: !135, line: 308, type: !262, flags: DIFlagPrototyped, spFlags: 0)
!262 = !DISubroutineType(types: !263)
!263 = !{!11, !160, !167, !11, !191}
!264 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !265, file: !132, line: 137)
!265 = !DISubprogram(name: "sprintf", scope: !135, file: !135, line: 334, type: !266, flags: DIFlagPrototyped, spFlags: 0)
!266 = !DISubroutineType(types: !267)
!267 = !{!11, !167, !172, null}
!268 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !269, file: !132, line: 138)
!269 = !DISubprogram(name: "sscanf", linkageName: "__isoc99_sscanf", scope: !135, file: !135, line: 412, type: !270, flags: DIFlagPrototyped, spFlags: 0)
!270 = !DISubroutineType(types: !271)
!271 = !{!11, !172, !172, null}
!272 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !273, file: !132, line: 139)
!273 = !DISubprogram(name: "tmpfile", scope: !135, file: !135, line: 173, type: !274, flags: DIFlagPrototyped, spFlags: 0)
!274 = !DISubroutineType(types: !275)
!275 = !{!143}
!276 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !277, file: !132, line: 141)
!277 = !DISubprogram(name: "tmpnam", scope: !135, file: !135, line: 187, type: !278, flags: DIFlagPrototyped, spFlags: 0)
!278 = !DISubroutineType(types: !279)
!279 = !{!35, !35}
!280 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !281, file: !132, line: 143)
!281 = !DISubprogram(name: "ungetc", scope: !135, file: !135, line: 639, type: !181, flags: DIFlagPrototyped, spFlags: 0)
!282 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !283, file: !132, line: 144)
!283 = !DISubprogram(name: "vfprintf", scope: !135, file: !135, line: 341, type: !284, flags: DIFlagPrototyped, spFlags: 0)
!284 = !DISubroutineType(types: !285)
!285 = !{!11, !160, !172, !286}
!286 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !287, size: 64)
!287 = distinct !DICompositeType(tag: DW_TAG_structure_type, name: "__va_list_tag", size: 192, flags: DIFlagTypePassByValue, elements: !288, identifier: "_ZTS13__va_list_tag")
!288 = !{!289, !290, !291, !292}
!289 = !DIDerivedType(tag: DW_TAG_member, name: "gp_offset", scope: !287, file: !31, baseType: !97, size: 32)
!290 = !DIDerivedType(tag: DW_TAG_member, name: "fp_offset", scope: !287, file: !31, baseType: !97, size: 32, offset: 32)
!291 = !DIDerivedType(tag: DW_TAG_member, name: "overflow_arg_area", scope: !287, file: !31, baseType: !194, size: 64, offset: 64)
!292 = !DIDerivedType(tag: DW_TAG_member, name: "reg_save_area", scope: !287, file: !31, baseType: !194, size: 64, offset: 128)
!293 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !294, file: !132, line: 145)
!294 = !DISubprogram(name: "vprintf", scope: !135, file: !135, line: 347, type: !295, flags: DIFlagPrototyped, spFlags: 0)
!295 = !DISubroutineType(types: !296)
!296 = !{!11, !172, !286}
!297 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !298, file: !132, line: 146)
!298 = !DISubprogram(name: "vsprintf", scope: !135, file: !135, line: 349, type: !299, flags: DIFlagPrototyped, spFlags: 0)
!299 = !DISubroutineType(types: !300)
!300 = !{!11, !167, !172, !286}
!301 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !303, file: !132, line: 175)
!302 = !DINamespace(name: "__gnu_cxx", scope: null)
!303 = !DISubprogram(name: "snprintf", scope: !135, file: !135, line: 354, type: !304, flags: DIFlagPrototyped, spFlags: 0)
!304 = !DISubroutineType(types: !305)
!305 = !{!11, !167, !191, !172, null}
!306 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !307, file: !132, line: 176)
!307 = !DISubprogram(name: "vfscanf", linkageName: "__isoc99_vfscanf", scope: !135, file: !135, line: 451, type: !284, flags: DIFlagPrototyped, spFlags: 0)
!308 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !309, file: !132, line: 177)
!309 = !DISubprogram(name: "vscanf", linkageName: "__isoc99_vscanf", scope: !135, file: !135, line: 456, type: !295, flags: DIFlagPrototyped, spFlags: 0)
!310 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !311, file: !132, line: 178)
!311 = !DISubprogram(name: "vsnprintf", scope: !135, file: !135, line: 358, type: !312, flags: DIFlagPrototyped, spFlags: 0)
!312 = !DISubroutineType(types: !313)
!313 = !{!11, !167, !191, !172, !286}
!314 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !315, file: !132, line: 179)
!315 = !DISubprogram(name: "vsscanf", linkageName: "__isoc99_vsscanf", scope: !135, file: !135, line: 459, type: !316, flags: DIFlagPrototyped, spFlags: 0)
!316 = !DISubroutineType(types: !317)
!317 = !{!11, !172, !172, !286}
!318 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !303, file: !132, line: 185)
!319 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !307, file: !132, line: 186)
!320 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !309, file: !132, line: 187)
!321 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !311, file: !132, line: 188)
!322 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !315, file: !132, line: 189)
!323 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !324, file: !326, line: 52)
!324 = !DISubprogram(name: "abs", scope: !325, file: !325, line: 840, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!325 = !DIFile(filename: "/usr/include/stdlib.h", directory: "")
!326 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/std_abs.h", directory: "")
!327 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !328, file: !330, line: 127)
!328 = !DIDerivedType(tag: DW_TAG_typedef, name: "div_t", file: !325, line: 62, baseType: !329)
!329 = !DICompositeType(tag: DW_TAG_structure_type, file: !325, line: 58, size: 64, flags: DIFlagFwdDecl, identifier: "_ZTS5div_t")
!330 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/cstdlib", directory: "")
!331 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !332, file: !330, line: 128)
!332 = !DIDerivedType(tag: DW_TAG_typedef, name: "ldiv_t", file: !325, line: 70, baseType: !333)
!333 = distinct !DICompositeType(tag: DW_TAG_structure_type, file: !325, line: 66, size: 128, flags: DIFlagTypePassByValue, elements: !334, identifier: "_ZTS6ldiv_t")
!334 = !{!335, !336}
!335 = !DIDerivedType(tag: DW_TAG_member, name: "quot", scope: !333, file: !325, line: 68, baseType: !58, size: 64)
!336 = !DIDerivedType(tag: DW_TAG_member, name: "rem", scope: !333, file: !325, line: 69, baseType: !58, size: 64, offset: 64)
!337 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !338, file: !330, line: 130)
!338 = !DISubprogram(name: "abort", scope: !325, file: !325, line: 591, type: !339, flags: DIFlagPrototyped | DIFlagNoReturn, spFlags: 0)
!339 = !DISubroutineType(types: !340)
!340 = !{null}
!341 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !342, file: !330, line: 134)
!342 = !DISubprogram(name: "atexit", scope: !325, file: !325, line: 595, type: !343, flags: DIFlagPrototyped, spFlags: 0)
!343 = !DISubroutineType(types: !344)
!344 = !{!11, !345}
!345 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !339, size: 64)
!346 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !347, file: !330, line: 137)
!347 = !DISubprogram(name: "at_quick_exit", scope: !325, file: !325, line: 600, type: !343, flags: DIFlagPrototyped, spFlags: 0)
!348 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !349, file: !330, line: 140)
!349 = !DISubprogram(name: "atof", scope: !325, file: !325, line: 101, type: !350, flags: DIFlagPrototyped, spFlags: 0)
!350 = !DISubroutineType(types: !351)
!351 = !{!352, !173}
!352 = !DIBasicType(name: "double", size: 64, encoding: DW_ATE_float)
!353 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !354, file: !330, line: 141)
!354 = !DISubprogram(name: "atoi", scope: !325, file: !325, line: 104, type: !244, flags: DIFlagPrototyped, spFlags: 0)
!355 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !356, file: !330, line: 142)
!356 = !DISubprogram(name: "atol", scope: !325, file: !325, line: 107, type: !357, flags: DIFlagPrototyped, spFlags: 0)
!357 = !DISubroutineType(types: !358)
!358 = !{!58, !173}
!359 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !360, file: !330, line: 143)
!360 = !DISubprogram(name: "bsearch", scope: !325, file: !325, line: 820, type: !361, flags: DIFlagPrototyped, spFlags: 0)
!361 = !DISubroutineType(types: !362)
!362 = !{!194, !220, !220, !191, !191, !363}
!363 = !DIDerivedType(tag: DW_TAG_typedef, name: "__compar_fn_t", file: !325, line: 808, baseType: !364)
!364 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !365, size: 64)
!365 = !DISubroutineType(types: !366)
!366 = !{!11, !220, !220}
!367 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !368, file: !330, line: 144)
!368 = !DISubprogram(name: "calloc", scope: !325, file: !325, line: 542, type: !369, flags: DIFlagPrototyped, spFlags: 0)
!369 = !DISubroutineType(types: !370)
!370 = !{!194, !191, !191}
!371 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !372, file: !330, line: 145)
!372 = !DISubprogram(name: "div", scope: !325, file: !325, line: 852, type: !373, flags: DIFlagPrototyped, spFlags: 0)
!373 = !DISubroutineType(types: !374)
!374 = !{!328, !11, !11}
!375 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !376, file: !330, line: 146)
!376 = !DISubprogram(name: "exit", scope: !325, file: !325, line: 617, type: !377, flags: DIFlagPrototyped | DIFlagNoReturn, spFlags: 0)
!377 = !DISubroutineType(types: !378)
!378 = !{null, !11}
!379 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !380, file: !330, line: 147)
!380 = !DISubprogram(name: "free", scope: !325, file: !325, line: 565, type: !381, flags: DIFlagPrototyped, spFlags: 0)
!381 = !DISubroutineType(types: !382)
!382 = !{null, !194}
!383 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !384, file: !330, line: 148)
!384 = !DISubprogram(name: "getenv", scope: !325, file: !325, line: 634, type: !385, flags: DIFlagPrototyped, spFlags: 0)
!385 = !DISubroutineType(types: !386)
!386 = !{!35, !173}
!387 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !388, file: !330, line: 149)
!388 = !DISubprogram(name: "labs", scope: !325, file: !325, line: 841, type: !389, flags: DIFlagPrototyped, spFlags: 0)
!389 = !DISubroutineType(types: !390)
!390 = !{!58, !58}
!391 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !392, file: !330, line: 150)
!392 = !DISubprogram(name: "ldiv", scope: !325, file: !325, line: 854, type: !393, flags: DIFlagPrototyped, spFlags: 0)
!393 = !DISubroutineType(types: !394)
!394 = !{!332, !58, !58}
!395 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !396, file: !330, line: 151)
!396 = !DISubprogram(name: "malloc", scope: !325, file: !325, line: 539, type: !397, flags: DIFlagPrototyped, spFlags: 0)
!397 = !DISubroutineType(types: !398)
!398 = !{!194, !191}
!399 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !400, file: !330, line: 153)
!400 = !DISubprogram(name: "mblen", scope: !325, file: !325, line: 922, type: !401, flags: DIFlagPrototyped, spFlags: 0)
!401 = !DISubroutineType(types: !402)
!402 = !{!11, !173, !191}
!403 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !404, file: !330, line: 154)
!404 = !DISubprogram(name: "mbstowcs", scope: !325, file: !325, line: 933, type: !405, flags: DIFlagPrototyped, spFlags: 0)
!405 = !DISubroutineType(types: !406)
!406 = !{!191, !407, !172, !191}
!407 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !408)
!408 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !409, size: 64)
!409 = !DIBasicType(name: "wchar_t", size: 32, encoding: DW_ATE_signed)
!410 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !411, file: !330, line: 155)
!411 = !DISubprogram(name: "mbtowc", scope: !325, file: !325, line: 925, type: !412, flags: DIFlagPrototyped, spFlags: 0)
!412 = !DISubroutineType(types: !413)
!413 = !{!11, !407, !172, !191}
!414 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !415, file: !330, line: 157)
!415 = !DISubprogram(name: "qsort", scope: !325, file: !325, line: 830, type: !416, flags: DIFlagPrototyped, spFlags: 0)
!416 = !DISubroutineType(types: !417)
!417 = !{null, !194, !191, !191, !363}
!418 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !419, file: !330, line: 160)
!419 = !DISubprogram(name: "quick_exit", scope: !325, file: !325, line: 623, type: !377, flags: DIFlagPrototyped | DIFlagNoReturn, spFlags: 0)
!420 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !421, file: !330, line: 163)
!421 = !DISubprogram(name: "rand", scope: !325, file: !325, line: 453, type: !226, flags: DIFlagPrototyped, spFlags: 0)
!422 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !423, file: !330, line: 164)
!423 = !DISubprogram(name: "realloc", scope: !325, file: !325, line: 550, type: !424, flags: DIFlagPrototyped, spFlags: 0)
!424 = !DISubroutineType(types: !425)
!425 = !{!194, !194, !191}
!426 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !427, file: !330, line: 165)
!427 = !DISubprogram(name: "srand", scope: !325, file: !325, line: 455, type: !428, flags: DIFlagPrototyped, spFlags: 0)
!428 = !DISubroutineType(types: !429)
!429 = !{null, !97}
!430 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !431, file: !330, line: 166)
!431 = !DISubprogram(name: "strtod", scope: !325, file: !325, line: 117, type: !432, flags: DIFlagPrototyped, spFlags: 0)
!432 = !DISubroutineType(types: !433)
!433 = !{!352, !172, !434}
!434 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !34)
!435 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !436, file: !330, line: 167)
!436 = !DISubprogram(name: "strtol", scope: !325, file: !325, line: 176, type: !437, flags: DIFlagPrototyped, spFlags: 0)
!437 = !DISubroutineType(types: !438)
!438 = !{!58, !172, !434, !11}
!439 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !440, file: !330, line: 168)
!440 = !DISubprogram(name: "strtoul", scope: !325, file: !325, line: 180, type: !441, flags: DIFlagPrototyped, spFlags: 0)
!441 = !DISubroutineType(types: !442)
!442 = !{!101, !172, !434, !11}
!443 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !444, file: !330, line: 169)
!444 = !DISubprogram(name: "system", scope: !325, file: !325, line: 784, type: !244, flags: DIFlagPrototyped, spFlags: 0)
!445 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !446, file: !330, line: 171)
!446 = !DISubprogram(name: "wcstombs", scope: !325, file: !325, line: 936, type: !447, flags: DIFlagPrototyped, spFlags: 0)
!447 = !DISubroutineType(types: !448)
!448 = !{!191, !167, !449, !191}
!449 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !450)
!450 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !451, size: 64)
!451 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !409)
!452 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !453, file: !330, line: 172)
!453 = !DISubprogram(name: "wctomb", scope: !325, file: !325, line: 929, type: !454, flags: DIFlagPrototyped, spFlags: 0)
!454 = !DISubroutineType(types: !455)
!455 = !{!11, !35, !409}
!456 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !457, file: !330, line: 200)
!457 = !DIDerivedType(tag: DW_TAG_typedef, name: "lldiv_t", file: !325, line: 80, baseType: !458)
!458 = distinct !DICompositeType(tag: DW_TAG_structure_type, file: !325, line: 76, size: 128, flags: DIFlagTypePassByValue, elements: !459, identifier: "_ZTS7lldiv_t")
!459 = !{!460, !462}
!460 = !DIDerivedType(tag: DW_TAG_member, name: "quot", scope: !458, file: !325, line: 78, baseType: !461, size: 64)
!461 = !DIBasicType(name: "long long int", size: 64, encoding: DW_ATE_signed)
!462 = !DIDerivedType(tag: DW_TAG_member, name: "rem", scope: !458, file: !325, line: 79, baseType: !461, size: 64, offset: 64)
!463 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !464, file: !330, line: 206)
!464 = !DISubprogram(name: "_Exit", scope: !325, file: !325, line: 629, type: !377, flags: DIFlagPrototyped | DIFlagNoReturn, spFlags: 0)
!465 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !466, file: !330, line: 210)
!466 = !DISubprogram(name: "llabs", scope: !325, file: !325, line: 844, type: !467, flags: DIFlagPrototyped, spFlags: 0)
!467 = !DISubroutineType(types: !468)
!468 = !{!461, !461}
!469 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !470, file: !330, line: 216)
!470 = !DISubprogram(name: "lldiv", scope: !325, file: !325, line: 858, type: !471, flags: DIFlagPrototyped, spFlags: 0)
!471 = !DISubroutineType(types: !472)
!472 = !{!457, !461, !461}
!473 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !474, file: !330, line: 227)
!474 = !DISubprogram(name: "atoll", scope: !325, file: !325, line: 112, type: !475, flags: DIFlagPrototyped, spFlags: 0)
!475 = !DISubroutineType(types: !476)
!476 = !{!461, !173}
!477 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !478, file: !330, line: 228)
!478 = !DISubprogram(name: "strtoll", scope: !325, file: !325, line: 200, type: !479, flags: DIFlagPrototyped, spFlags: 0)
!479 = !DISubroutineType(types: !480)
!480 = !{!461, !172, !434, !11}
!481 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !482, file: !330, line: 229)
!482 = !DISubprogram(name: "strtoull", scope: !325, file: !325, line: 205, type: !483, flags: DIFlagPrototyped, spFlags: 0)
!483 = !DISubroutineType(types: !484)
!484 = !{!485, !172, !434, !11}
!485 = !DIBasicType(name: "long long unsigned int", size: 64, encoding: DW_ATE_unsigned)
!486 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !487, file: !330, line: 231)
!487 = !DISubprogram(name: "strtof", scope: !325, file: !325, line: 123, type: !488, flags: DIFlagPrototyped, spFlags: 0)
!488 = !DISubroutineType(types: !489)
!489 = !{!490, !172, !434}
!490 = !DIBasicType(name: "float", size: 32, encoding: DW_ATE_float)
!491 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !492, file: !330, line: 232)
!492 = !DISubprogram(name: "strtold", scope: !325, file: !325, line: 126, type: !493, flags: DIFlagPrototyped, spFlags: 0)
!493 = !DISubroutineType(types: !494)
!494 = !{!495, !172, !434}
!495 = !DIBasicType(name: "long double", size: 128, encoding: DW_ATE_float)
!496 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !457, file: !330, line: 240)
!497 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !464, file: !330, line: 242)
!498 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !466, file: !330, line: 244)
!499 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !500, file: !330, line: 245)
!500 = !DISubprogram(name: "div", linkageName: "_ZN9__gnu_cxx3divExx", scope: !302, file: !330, line: 213, type: !471, flags: DIFlagPrototyped, spFlags: 0)
!501 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !470, file: !330, line: 246)
!502 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !474, file: !330, line: 248)
!503 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !487, file: !330, line: 249)
!504 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !478, file: !330, line: 250)
!505 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !482, file: !330, line: 251)
!506 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !492, file: !330, line: 252)
!507 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !508, file: !512, line: 77)
!508 = !DISubprogram(name: "memchr", scope: !509, file: !509, line: 73, type: !510, flags: DIFlagPrototyped, spFlags: 0)
!509 = !DIFile(filename: "/usr/include/string.h", directory: "")
!510 = !DISubroutineType(types: !511)
!511 = !{!220, !220, !11, !191}
!512 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/cstring", directory: "")
!513 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !514, file: !512, line: 78)
!514 = !DISubprogram(name: "memcmp", scope: !509, file: !509, line: 64, type: !515, flags: DIFlagPrototyped, spFlags: 0)
!515 = !DISubroutineType(types: !516)
!516 = !{!11, !220, !220, !191}
!517 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !518, file: !512, line: 79)
!518 = !DISubprogram(name: "memcpy", scope: !509, file: !509, line: 43, type: !519, flags: DIFlagPrototyped, spFlags: 0)
!519 = !DISubroutineType(types: !520)
!520 = !{!194, !193, !219, !191}
!521 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !522, file: !512, line: 80)
!522 = !DISubprogram(name: "memmove", scope: !509, file: !509, line: 47, type: !523, flags: DIFlagPrototyped, spFlags: 0)
!523 = !DISubroutineType(types: !524)
!524 = !{!194, !194, !220, !191}
!525 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !526, file: !512, line: 81)
!526 = !DISubprogram(name: "memset", scope: !509, file: !509, line: 61, type: !527, flags: DIFlagPrototyped, spFlags: 0)
!527 = !DISubroutineType(types: !528)
!528 = !{!194, !194, !11, !191}
!529 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !530, file: !512, line: 82)
!530 = !DISubprogram(name: "strcat", scope: !509, file: !509, line: 130, type: !531, flags: DIFlagPrototyped, spFlags: 0)
!531 = !DISubroutineType(types: !532)
!532 = !{!35, !167, !172}
!533 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !534, file: !512, line: 83)
!534 = !DISubprogram(name: "strcmp", scope: !509, file: !509, line: 137, type: !250, flags: DIFlagPrototyped, spFlags: 0)
!535 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !536, file: !512, line: 84)
!536 = !DISubprogram(name: "strcoll", scope: !509, file: !509, line: 144, type: !250, flags: DIFlagPrototyped, spFlags: 0)
!537 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !538, file: !512, line: 85)
!538 = !DISubprogram(name: "strcpy", scope: !509, file: !509, line: 122, type: !531, flags: DIFlagPrototyped, spFlags: 0)
!539 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !540, file: !512, line: 86)
!540 = !DISubprogram(name: "strcspn", scope: !509, file: !509, line: 273, type: !541, flags: DIFlagPrototyped, spFlags: 0)
!541 = !DISubroutineType(types: !542)
!542 = !{!191, !173, !173}
!543 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !544, file: !512, line: 87)
!544 = !DISubprogram(name: "strerror", scope: !509, file: !509, line: 397, type: !545, flags: DIFlagPrototyped, spFlags: 0)
!545 = !DISubroutineType(types: !546)
!546 = !{!35, !11}
!547 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !548, file: !512, line: 88)
!548 = !DISubprogram(name: "strlen", scope: !509, file: !509, line: 385, type: !549, flags: DIFlagPrototyped, spFlags: 0)
!549 = !DISubroutineType(types: !550)
!550 = !{!191, !173}
!551 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !552, file: !512, line: 89)
!552 = !DISubprogram(name: "strncat", scope: !509, file: !509, line: 133, type: !553, flags: DIFlagPrototyped, spFlags: 0)
!553 = !DISubroutineType(types: !554)
!554 = !{!35, !167, !172, !191}
!555 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !556, file: !512, line: 90)
!556 = !DISubprogram(name: "strncmp", scope: !509, file: !509, line: 140, type: !557, flags: DIFlagPrototyped, spFlags: 0)
!557 = !DISubroutineType(types: !558)
!558 = !{!11, !173, !173, !191}
!559 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !560, file: !512, line: 91)
!560 = !DISubprogram(name: "strncpy", scope: !509, file: !509, line: 125, type: !553, flags: DIFlagPrototyped, spFlags: 0)
!561 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !562, file: !512, line: 92)
!562 = !DISubprogram(name: "strspn", scope: !509, file: !509, line: 277, type: !541, flags: DIFlagPrototyped, spFlags: 0)
!563 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !564, file: !512, line: 93)
!564 = !DISubprogram(name: "strtok", scope: !509, file: !509, line: 336, type: !531, flags: DIFlagPrototyped, spFlags: 0)
!565 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !566, file: !512, line: 94)
!566 = !DISubprogram(name: "strxfrm", scope: !509, file: !509, line: 147, type: !567, flags: DIFlagPrototyped, spFlags: 0)
!567 = !DISubroutineType(types: !568)
!568 = !{!191, !167, !172, !191}
!569 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !570, file: !512, line: 95)
!570 = !DISubprogram(name: "strchr", scope: !509, file: !509, line: 208, type: !571, flags: DIFlagPrototyped, spFlags: 0)
!571 = !DISubroutineType(types: !572)
!572 = !{!173, !173, !11}
!573 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !574, file: !512, line: 96)
!574 = !DISubprogram(name: "strpbrk", scope: !509, file: !509, line: 285, type: !575, flags: DIFlagPrototyped, spFlags: 0)
!575 = !DISubroutineType(types: !576)
!576 = !{!173, !173, !173}
!577 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !578, file: !512, line: 97)
!578 = !DISubprogram(name: "strrchr", scope: !509, file: !509, line: 235, type: !571, flags: DIFlagPrototyped, spFlags: 0)
!579 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !580, file: !512, line: 98)
!580 = !DISubprogram(name: "strstr", scope: !509, file: !509, line: 312, type: !575, flags: DIFlagPrototyped, spFlags: 0)
!581 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !582, file: !597, line: 64)
!582 = !DIDerivedType(tag: DW_TAG_typedef, name: "mbstate_t", file: !583, line: 6, baseType: !584)
!583 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/types/mbstate_t.h", directory: "")
!584 = !DIDerivedType(tag: DW_TAG_typedef, name: "__mbstate_t", file: !585, line: 21, baseType: !586)
!585 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/types/__mbstate_t.h", directory: "")
!586 = distinct !DICompositeType(tag: DW_TAG_structure_type, file: !585, line: 13, size: 64, flags: DIFlagTypePassByValue, elements: !587, identifier: "_ZTS11__mbstate_t")
!587 = !{!588, !589}
!588 = !DIDerivedType(tag: DW_TAG_member, name: "__count", scope: !586, file: !585, line: 15, baseType: !11, size: 32)
!589 = !DIDerivedType(tag: DW_TAG_member, name: "__value", scope: !586, file: !585, line: 20, baseType: !590, size: 32, offset: 32)
!590 = distinct !DICompositeType(tag: DW_TAG_union_type, scope: !586, file: !585, line: 16, size: 32, flags: DIFlagTypePassByValue, elements: !591, identifier: "_ZTSN11__mbstate_tUt_E")
!591 = !{!592, !593}
!592 = !DIDerivedType(tag: DW_TAG_member, name: "__wch", scope: !590, file: !585, line: 18, baseType: !97, size: 32)
!593 = !DIDerivedType(tag: DW_TAG_member, name: "__wchb", scope: !590, file: !585, line: 19, baseType: !594, size: 32)
!594 = !DICompositeType(tag: DW_TAG_array_type, baseType: !36, size: 32, elements: !595)
!595 = !{!596}
!596 = !DISubrange(count: 4)
!597 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/cwchar", directory: "")
!598 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !599, file: !597, line: 141)
!599 = !DIDerivedType(tag: DW_TAG_typedef, name: "wint_t", file: !600, line: 20, baseType: !97)
!600 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/types/wint_t.h", directory: "")
!601 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !602, file: !597, line: 143)
!602 = !DISubprogram(name: "btowc", scope: !603, file: !603, line: 284, type: !604, flags: DIFlagPrototyped, spFlags: 0)
!603 = !DIFile(filename: "/usr/include/wchar.h", directory: "")
!604 = !DISubroutineType(types: !605)
!605 = !{!599, !11}
!606 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !607, file: !597, line: 144)
!607 = !DISubprogram(name: "fgetwc", scope: !603, file: !603, line: 726, type: !608, flags: DIFlagPrototyped, spFlags: 0)
!608 = !DISubroutineType(types: !609)
!609 = !{!599, !610}
!610 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !611, size: 64)
!611 = !DIDerivedType(tag: DW_TAG_typedef, name: "__FILE", file: !612, line: 5, baseType: !130)
!612 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/types/__FILE.h", directory: "")
!613 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !614, file: !597, line: 145)
!614 = !DISubprogram(name: "fgetws", scope: !603, file: !603, line: 755, type: !615, flags: DIFlagPrototyped, spFlags: 0)
!615 = !DISubroutineType(types: !616)
!616 = !{!408, !407, !11, !617}
!617 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !610)
!618 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !619, file: !597, line: 146)
!619 = !DISubprogram(name: "fputwc", scope: !603, file: !603, line: 740, type: !620, flags: DIFlagPrototyped, spFlags: 0)
!620 = !DISubroutineType(types: !621)
!621 = !{!599, !409, !610}
!622 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !623, file: !597, line: 147)
!623 = !DISubprogram(name: "fputws", scope: !603, file: !603, line: 762, type: !624, flags: DIFlagPrototyped, spFlags: 0)
!624 = !DISubroutineType(types: !625)
!625 = !{!11, !449, !617}
!626 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !627, file: !597, line: 148)
!627 = !DISubprogram(name: "fwide", scope: !603, file: !603, line: 573, type: !628, flags: DIFlagPrototyped, spFlags: 0)
!628 = !DISubroutineType(types: !629)
!629 = !{!11, !610, !11}
!630 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !631, file: !597, line: 149)
!631 = !DISubprogram(name: "fwprintf", scope: !603, file: !603, line: 580, type: !632, flags: DIFlagPrototyped, spFlags: 0)
!632 = !DISubroutineType(types: !633)
!633 = !{!11, !617, !449, null}
!634 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !635, file: !597, line: 150)
!635 = !DISubprogram(name: "fwscanf", linkageName: "__isoc99_fwscanf", scope: !603, file: !603, line: 640, type: !632, flags: DIFlagPrototyped, spFlags: 0)
!636 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !637, file: !597, line: 151)
!637 = !DISubprogram(name: "getwc", scope: !603, file: !603, line: 727, type: !608, flags: DIFlagPrototyped, spFlags: 0)
!638 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !639, file: !597, line: 152)
!639 = !DISubprogram(name: "getwchar", scope: !603, file: !603, line: 733, type: !640, flags: DIFlagPrototyped, spFlags: 0)
!640 = !DISubroutineType(types: !641)
!641 = !{!599}
!642 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !643, file: !597, line: 153)
!643 = !DISubprogram(name: "mbrlen", scope: !603, file: !603, line: 307, type: !644, flags: DIFlagPrototyped, spFlags: 0)
!644 = !DISubroutineType(types: !645)
!645 = !{!191, !172, !191, !646}
!646 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !647)
!647 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !582, size: 64)
!648 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !649, file: !597, line: 154)
!649 = !DISubprogram(name: "mbrtowc", scope: !603, file: !603, line: 296, type: !650, flags: DIFlagPrototyped, spFlags: 0)
!650 = !DISubroutineType(types: !651)
!651 = !{!191, !407, !172, !191, !646}
!652 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !653, file: !597, line: 155)
!653 = !DISubprogram(name: "mbsinit", scope: !603, file: !603, line: 292, type: !654, flags: DIFlagPrototyped, spFlags: 0)
!654 = !DISubroutineType(types: !655)
!655 = !{!11, !656}
!656 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !657, size: 64)
!657 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !582)
!658 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !659, file: !597, line: 156)
!659 = !DISubprogram(name: "mbsrtowcs", scope: !603, file: !603, line: 337, type: !660, flags: DIFlagPrototyped, spFlags: 0)
!660 = !DISubroutineType(types: !661)
!661 = !{!191, !407, !662, !191, !646}
!662 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !663)
!663 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !173, size: 64)
!664 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !665, file: !597, line: 157)
!665 = !DISubprogram(name: "putwc", scope: !603, file: !603, line: 741, type: !620, flags: DIFlagPrototyped, spFlags: 0)
!666 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !667, file: !597, line: 158)
!667 = !DISubprogram(name: "putwchar", scope: !603, file: !603, line: 747, type: !668, flags: DIFlagPrototyped, spFlags: 0)
!668 = !DISubroutineType(types: !669)
!669 = !{!599, !409}
!670 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !671, file: !597, line: 160)
!671 = !DISubprogram(name: "swprintf", scope: !603, file: !603, line: 590, type: !672, flags: DIFlagPrototyped, spFlags: 0)
!672 = !DISubroutineType(types: !673)
!673 = !{!11, !407, !191, !449, null}
!674 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !675, file: !597, line: 162)
!675 = !DISubprogram(name: "swscanf", linkageName: "__isoc99_swscanf", scope: !603, file: !603, line: 647, type: !676, flags: DIFlagPrototyped, spFlags: 0)
!676 = !DISubroutineType(types: !677)
!677 = !{!11, !449, !449, null}
!678 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !679, file: !597, line: 163)
!679 = !DISubprogram(name: "ungetwc", scope: !603, file: !603, line: 770, type: !680, flags: DIFlagPrototyped, spFlags: 0)
!680 = !DISubroutineType(types: !681)
!681 = !{!599, !599, !610}
!682 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !683, file: !597, line: 164)
!683 = !DISubprogram(name: "vfwprintf", scope: !603, file: !603, line: 598, type: !684, flags: DIFlagPrototyped, spFlags: 0)
!684 = !DISubroutineType(types: !685)
!685 = !{!11, !617, !449, !286}
!686 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !687, file: !597, line: 166)
!687 = !DISubprogram(name: "vfwscanf", linkageName: "__isoc99_vfwscanf", scope: !603, file: !603, line: 693, type: !684, flags: DIFlagPrototyped, spFlags: 0)
!688 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !689, file: !597, line: 169)
!689 = !DISubprogram(name: "vswprintf", scope: !603, file: !603, line: 611, type: !690, flags: DIFlagPrototyped, spFlags: 0)
!690 = !DISubroutineType(types: !691)
!691 = !{!11, !407, !191, !449, !286}
!692 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !693, file: !597, line: 172)
!693 = !DISubprogram(name: "vswscanf", linkageName: "__isoc99_vswscanf", scope: !603, file: !603, line: 700, type: !694, flags: DIFlagPrototyped, spFlags: 0)
!694 = !DISubroutineType(types: !695)
!695 = !{!11, !449, !449, !286}
!696 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !697, file: !597, line: 174)
!697 = !DISubprogram(name: "vwprintf", scope: !603, file: !603, line: 606, type: !698, flags: DIFlagPrototyped, spFlags: 0)
!698 = !DISubroutineType(types: !699)
!699 = !{!11, !449, !286}
!700 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !701, file: !597, line: 176)
!701 = !DISubprogram(name: "vwscanf", linkageName: "__isoc99_vwscanf", scope: !603, file: !603, line: 697, type: !698, flags: DIFlagPrototyped, spFlags: 0)
!702 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !703, file: !597, line: 178)
!703 = !DISubprogram(name: "wcrtomb", scope: !603, file: !603, line: 301, type: !704, flags: DIFlagPrototyped, spFlags: 0)
!704 = !DISubroutineType(types: !705)
!705 = !{!191, !167, !409, !646}
!706 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !707, file: !597, line: 179)
!707 = !DISubprogram(name: "wcscat", scope: !603, file: !603, line: 97, type: !708, flags: DIFlagPrototyped, spFlags: 0)
!708 = !DISubroutineType(types: !709)
!709 = !{!408, !407, !449}
!710 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !711, file: !597, line: 180)
!711 = !DISubprogram(name: "wcscmp", scope: !603, file: !603, line: 106, type: !712, flags: DIFlagPrototyped, spFlags: 0)
!712 = !DISubroutineType(types: !713)
!713 = !{!11, !450, !450}
!714 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !715, file: !597, line: 181)
!715 = !DISubprogram(name: "wcscoll", scope: !603, file: !603, line: 131, type: !712, flags: DIFlagPrototyped, spFlags: 0)
!716 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !717, file: !597, line: 182)
!717 = !DISubprogram(name: "wcscpy", scope: !603, file: !603, line: 87, type: !708, flags: DIFlagPrototyped, spFlags: 0)
!718 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !719, file: !597, line: 183)
!719 = !DISubprogram(name: "wcscspn", scope: !603, file: !603, line: 187, type: !720, flags: DIFlagPrototyped, spFlags: 0)
!720 = !DISubroutineType(types: !721)
!721 = !{!191, !450, !450}
!722 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !723, file: !597, line: 184)
!723 = !DISubprogram(name: "wcsftime", scope: !603, file: !603, line: 834, type: !724, flags: DIFlagPrototyped, spFlags: 0)
!724 = !DISubroutineType(types: !725)
!725 = !{!191, !407, !191, !449, !726}
!726 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !727)
!727 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !728, size: 64)
!728 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !729)
!729 = !DICompositeType(tag: DW_TAG_structure_type, name: "tm", file: !603, line: 83, flags: DIFlagFwdDecl | DIFlagNonTrivial, identifier: "_ZTS2tm")
!730 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !731, file: !597, line: 185)
!731 = !DISubprogram(name: "wcslen", scope: !603, file: !603, line: 222, type: !732, flags: DIFlagPrototyped, spFlags: 0)
!732 = !DISubroutineType(types: !733)
!733 = !{!191, !450}
!734 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !735, file: !597, line: 186)
!735 = !DISubprogram(name: "wcsncat", scope: !603, file: !603, line: 101, type: !736, flags: DIFlagPrototyped, spFlags: 0)
!736 = !DISubroutineType(types: !737)
!737 = !{!408, !407, !449, !191}
!738 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !739, file: !597, line: 187)
!739 = !DISubprogram(name: "wcsncmp", scope: !603, file: !603, line: 109, type: !740, flags: DIFlagPrototyped, spFlags: 0)
!740 = !DISubroutineType(types: !741)
!741 = !{!11, !450, !450, !191}
!742 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !743, file: !597, line: 188)
!743 = !DISubprogram(name: "wcsncpy", scope: !603, file: !603, line: 92, type: !736, flags: DIFlagPrototyped, spFlags: 0)
!744 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !745, file: !597, line: 189)
!745 = !DISubprogram(name: "wcsrtombs", scope: !603, file: !603, line: 343, type: !746, flags: DIFlagPrototyped, spFlags: 0)
!746 = !DISubroutineType(types: !747)
!747 = !{!191, !167, !748, !191, !646}
!748 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !749)
!749 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !450, size: 64)
!750 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !751, file: !597, line: 190)
!751 = !DISubprogram(name: "wcsspn", scope: !603, file: !603, line: 191, type: !720, flags: DIFlagPrototyped, spFlags: 0)
!752 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !753, file: !597, line: 191)
!753 = !DISubprogram(name: "wcstod", scope: !603, file: !603, line: 377, type: !754, flags: DIFlagPrototyped, spFlags: 0)
!754 = !DISubroutineType(types: !755)
!755 = !{!352, !449, !756}
!756 = !DIDerivedType(tag: DW_TAG_restrict_type, baseType: !757)
!757 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !408, size: 64)
!758 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !759, file: !597, line: 193)
!759 = !DISubprogram(name: "wcstof", scope: !603, file: !603, line: 382, type: !760, flags: DIFlagPrototyped, spFlags: 0)
!760 = !DISubroutineType(types: !761)
!761 = !{!490, !449, !756}
!762 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !763, file: !597, line: 195)
!763 = !DISubprogram(name: "wcstok", scope: !603, file: !603, line: 217, type: !764, flags: DIFlagPrototyped, spFlags: 0)
!764 = !DISubroutineType(types: !765)
!765 = !{!408, !407, !449, !756}
!766 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !767, file: !597, line: 196)
!767 = !DISubprogram(name: "wcstol", scope: !603, file: !603, line: 428, type: !768, flags: DIFlagPrototyped, spFlags: 0)
!768 = !DISubroutineType(types: !769)
!769 = !{!58, !449, !756, !11}
!770 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !771, file: !597, line: 197)
!771 = !DISubprogram(name: "wcstoul", scope: !603, file: !603, line: 433, type: !772, flags: DIFlagPrototyped, spFlags: 0)
!772 = !DISubroutineType(types: !773)
!773 = !{!101, !449, !756, !11}
!774 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !775, file: !597, line: 198)
!775 = !DISubprogram(name: "wcsxfrm", scope: !603, file: !603, line: 135, type: !776, flags: DIFlagPrototyped, spFlags: 0)
!776 = !DISubroutineType(types: !777)
!777 = !{!191, !407, !449, !191}
!778 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !779, file: !597, line: 199)
!779 = !DISubprogram(name: "wctob", scope: !603, file: !603, line: 288, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!780 = !DISubroutineType(types: !781)
!781 = !{!11, !599}
!782 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !783, file: !597, line: 200)
!783 = !DISubprogram(name: "wmemcmp", scope: !603, file: !603, line: 258, type: !740, flags: DIFlagPrototyped, spFlags: 0)
!784 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !785, file: !597, line: 201)
!785 = !DISubprogram(name: "wmemcpy", scope: !603, file: !603, line: 262, type: !736, flags: DIFlagPrototyped, spFlags: 0)
!786 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !787, file: !597, line: 202)
!787 = !DISubprogram(name: "wmemmove", scope: !603, file: !603, line: 267, type: !788, flags: DIFlagPrototyped, spFlags: 0)
!788 = !DISubroutineType(types: !789)
!789 = !{!408, !408, !450, !191}
!790 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !791, file: !597, line: 203)
!791 = !DISubprogram(name: "wmemset", scope: !603, file: !603, line: 271, type: !792, flags: DIFlagPrototyped, spFlags: 0)
!792 = !DISubroutineType(types: !793)
!793 = !{!408, !408, !409, !191}
!794 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !795, file: !597, line: 204)
!795 = !DISubprogram(name: "wprintf", scope: !603, file: !603, line: 587, type: !796, flags: DIFlagPrototyped, spFlags: 0)
!796 = !DISubroutineType(types: !797)
!797 = !{!11, !449, null}
!798 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !799, file: !597, line: 205)
!799 = !DISubprogram(name: "wscanf", linkageName: "__isoc99_wscanf", scope: !603, file: !603, line: 644, type: !796, flags: DIFlagPrototyped, spFlags: 0)
!800 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !801, file: !597, line: 206)
!801 = !DISubprogram(name: "wcschr", scope: !603, file: !603, line: 164, type: !802, flags: DIFlagPrototyped, spFlags: 0)
!802 = !DISubroutineType(types: !803)
!803 = !{!408, !450, !409}
!804 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !805, file: !597, line: 207)
!805 = !DISubprogram(name: "wcspbrk", scope: !603, file: !603, line: 201, type: !806, flags: DIFlagPrototyped, spFlags: 0)
!806 = !DISubroutineType(types: !807)
!807 = !{!408, !450, !450}
!808 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !809, file: !597, line: 208)
!809 = !DISubprogram(name: "wcsrchr", scope: !603, file: !603, line: 174, type: !802, flags: DIFlagPrototyped, spFlags: 0)
!810 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !811, file: !597, line: 209)
!811 = !DISubprogram(name: "wcsstr", scope: !603, file: !603, line: 212, type: !806, flags: DIFlagPrototyped, spFlags: 0)
!812 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !813, file: !597, line: 210)
!813 = !DISubprogram(name: "wmemchr", scope: !603, file: !603, line: 253, type: !814, flags: DIFlagPrototyped, spFlags: 0)
!814 = !DISubroutineType(types: !815)
!815 = !{!408, !450, !409, !191}
!816 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !817, file: !597, line: 251)
!817 = !DISubprogram(name: "wcstold", scope: !603, file: !603, line: 384, type: !818, flags: DIFlagPrototyped, spFlags: 0)
!818 = !DISubroutineType(types: !819)
!819 = !{!495, !449, !756}
!820 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !821, file: !597, line: 260)
!821 = !DISubprogram(name: "wcstoll", scope: !603, file: !603, line: 441, type: !822, flags: DIFlagPrototyped, spFlags: 0)
!822 = !DISubroutineType(types: !823)
!823 = !{!461, !449, !756, !11}
!824 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !825, file: !597, line: 261)
!825 = !DISubprogram(name: "wcstoull", scope: !603, file: !603, line: 448, type: !826, flags: DIFlagPrototyped, spFlags: 0)
!826 = !DISubroutineType(types: !827)
!827 = !{!485, !449, !756, !11}
!828 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !817, file: !597, line: 267)
!829 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !821, file: !597, line: 268)
!830 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !825, file: !597, line: 269)
!831 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !759, file: !597, line: 283)
!832 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !687, file: !597, line: 286)
!833 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !693, file: !597, line: 289)
!834 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !701, file: !597, line: 292)
!835 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !817, file: !597, line: 296)
!836 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !821, file: !597, line: 297)
!837 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !825, file: !597, line: 298)
!838 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !839, file: !840, line: 57)
!839 = distinct !DICompositeType(tag: DW_TAG_class_type, name: "exception_ptr", scope: !841, file: !840, line: 79, size: 64, flags: DIFlagTypePassByReference | DIFlagNonTrivial, elements: !842, identifier: "_ZTSNSt15__exception_ptr13exception_ptrE")
!840 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/exception_ptr.h", directory: "")
!841 = !DINamespace(name: "__exception_ptr", scope: !2)
!842 = !{!843, !844, !848, !851, !852, !857, !858, !862, !868, !872, !876, !879, !880, !883, !886}
!843 = !DIDerivedType(tag: DW_TAG_member, name: "_M_exception_object", scope: !839, file: !840, line: 81, baseType: !194, size: 64)
!844 = !DISubprogram(name: "exception_ptr", scope: !839, file: !840, line: 83, type: !845, scopeLine: 83, flags: DIFlagExplicit | DIFlagPrototyped, spFlags: 0)
!845 = !DISubroutineType(types: !846)
!846 = !{null, !847, !194}
!847 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !839, size: 64, flags: DIFlagArtificial | DIFlagObjectPointer)
!848 = !DISubprogram(name: "_M_addref", linkageName: "_ZNSt15__exception_ptr13exception_ptr9_M_addrefEv", scope: !839, file: !840, line: 85, type: !849, scopeLine: 85, flags: DIFlagPrototyped, spFlags: 0)
!849 = !DISubroutineType(types: !850)
!850 = !{null, !847}
!851 = !DISubprogram(name: "_M_release", linkageName: "_ZNSt15__exception_ptr13exception_ptr10_M_releaseEv", scope: !839, file: !840, line: 86, type: !849, scopeLine: 86, flags: DIFlagPrototyped, spFlags: 0)
!852 = !DISubprogram(name: "_M_get", linkageName: "_ZNKSt15__exception_ptr13exception_ptr6_M_getEv", scope: !839, file: !840, line: 88, type: !853, scopeLine: 88, flags: DIFlagPrototyped, spFlags: 0)
!853 = !DISubroutineType(types: !854)
!854 = !{!194, !855}
!855 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !856, size: 64, flags: DIFlagArtificial | DIFlagObjectPointer)
!856 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !839)
!857 = !DISubprogram(name: "exception_ptr", scope: !839, file: !840, line: 96, type: !849, scopeLine: 96, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!858 = !DISubprogram(name: "exception_ptr", scope: !839, file: !840, line: 98, type: !859, scopeLine: 98, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!859 = !DISubroutineType(types: !860)
!860 = !{null, !847, !861}
!861 = !DIDerivedType(tag: DW_TAG_reference_type, baseType: !856, size: 64)
!862 = !DISubprogram(name: "exception_ptr", scope: !839, file: !840, line: 101, type: !863, scopeLine: 101, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!863 = !DISubroutineType(types: !864)
!864 = !{null, !847, !865}
!865 = !DIDerivedType(tag: DW_TAG_typedef, name: "nullptr_t", scope: !2, file: !866, line: 262, baseType: !867)
!866 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/x86_64-linux-gnu/c++/9/bits/c++config.h", directory: "")
!867 = !DIBasicType(tag: DW_TAG_unspecified_type, name: "decltype(nullptr)")
!868 = !DISubprogram(name: "exception_ptr", scope: !839, file: !840, line: 105, type: !869, scopeLine: 105, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!869 = !DISubroutineType(types: !870)
!870 = !{null, !847, !871}
!871 = !DIDerivedType(tag: DW_TAG_rvalue_reference_type, baseType: !839, size: 64)
!872 = !DISubprogram(name: "operator=", linkageName: "_ZNSt15__exception_ptr13exception_ptraSERKS0_", scope: !839, file: !840, line: 118, type: !873, scopeLine: 118, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!873 = !DISubroutineType(types: !874)
!874 = !{!875, !847, !861}
!875 = !DIDerivedType(tag: DW_TAG_reference_type, baseType: !839, size: 64)
!876 = !DISubprogram(name: "operator=", linkageName: "_ZNSt15__exception_ptr13exception_ptraSEOS0_", scope: !839, file: !840, line: 122, type: !877, scopeLine: 122, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!877 = !DISubroutineType(types: !878)
!878 = !{!875, !847, !871}
!879 = !DISubprogram(name: "~exception_ptr", scope: !839, file: !840, line: 129, type: !849, scopeLine: 129, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!880 = !DISubprogram(name: "swap", linkageName: "_ZNSt15__exception_ptr13exception_ptr4swapERS0_", scope: !839, file: !840, line: 132, type: !881, scopeLine: 132, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!881 = !DISubroutineType(types: !882)
!882 = !{null, !847, !875}
!883 = !DISubprogram(name: "operator bool", linkageName: "_ZNKSt15__exception_ptr13exception_ptrcvbEv", scope: !839, file: !840, line: 144, type: !884, scopeLine: 144, flags: DIFlagPublic | DIFlagExplicit | DIFlagPrototyped, spFlags: 0)
!884 = !DISubroutineType(types: !885)
!885 = !{!13, !855}
!886 = !DISubprogram(name: "__cxa_exception_type", linkageName: "_ZNKSt15__exception_ptr13exception_ptr20__cxa_exception_typeEv", scope: !839, file: !840, line: 153, type: !887, scopeLine: 153, flags: DIFlagPublic | DIFlagPrototyped, spFlags: 0)
!887 = !DISubroutineType(types: !888)
!888 = !{!889, !855}
!889 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !890, size: 64)
!890 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !891)
!891 = !DICompositeType(tag: DW_TAG_class_type, name: "type_info", scope: !2, file: !892, line: 88, size: 128, flags: DIFlagFwdDecl | DIFlagNonTrivial)
!892 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/typeinfo", directory: "")
!893 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !841, entity: !894, file: !840, line: 73)
!894 = !DISubprogram(name: "rethrow_exception", linkageName: "_ZSt17rethrow_exceptionNSt15__exception_ptr13exception_ptrE", scope: !2, file: !840, line: 69, type: !895, flags: DIFlagPrototyped | DIFlagNoReturn, spFlags: 0)
!895 = !DISubroutineType(types: !896)
!896 = !{null, !839}
!897 = !DIImportedEntity(tag: DW_TAG_imported_module, scope: !898, entity: !899, file: !900, line: 58)
!898 = !DINamespace(name: "__gnu_debug", scope: null)
!899 = !DINamespace(name: "__debug", scope: !2)
!900 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/debug/debug.h", directory: "")
!901 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !902, file: !904, line: 53)
!902 = !DICompositeType(tag: DW_TAG_structure_type, name: "lconv", file: !903, line: 51, size: 768, flags: DIFlagFwdDecl, identifier: "_ZTS5lconv")
!903 = !DIFile(filename: "/usr/include/locale.h", directory: "")
!904 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/clocale", directory: "")
!905 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !906, file: !904, line: 54)
!906 = !DISubprogram(name: "setlocale", scope: !903, file: !903, line: 122, type: !907, flags: DIFlagPrototyped, spFlags: 0)
!907 = !DISubroutineType(types: !908)
!908 = !{!35, !11, !173}
!909 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !910, file: !904, line: 55)
!910 = !DISubprogram(name: "localeconv", scope: !903, file: !903, line: 125, type: !911, flags: DIFlagPrototyped, spFlags: 0)
!911 = !DISubroutineType(types: !912)
!912 = !{!913}
!913 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !902, size: 64)
!914 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !915, file: !917, line: 64)
!915 = !DISubprogram(name: "isalnum", scope: !916, file: !916, line: 108, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!916 = !DIFile(filename: "/usr/include/ctype.h", directory: "")
!917 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/cctype", directory: "")
!918 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !919, file: !917, line: 65)
!919 = !DISubprogram(name: "isalpha", scope: !916, file: !916, line: 109, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!920 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !921, file: !917, line: 66)
!921 = !DISubprogram(name: "iscntrl", scope: !916, file: !916, line: 110, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!922 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !923, file: !917, line: 67)
!923 = !DISubprogram(name: "isdigit", scope: !916, file: !916, line: 111, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!924 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !925, file: !917, line: 68)
!925 = !DISubprogram(name: "isgraph", scope: !916, file: !916, line: 113, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!926 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !927, file: !917, line: 69)
!927 = !DISubprogram(name: "islower", scope: !916, file: !916, line: 112, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!928 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !929, file: !917, line: 70)
!929 = !DISubprogram(name: "isprint", scope: !916, file: !916, line: 114, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!930 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !931, file: !917, line: 71)
!931 = !DISubprogram(name: "ispunct", scope: !916, file: !916, line: 115, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!932 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !933, file: !917, line: 72)
!933 = !DISubprogram(name: "isspace", scope: !916, file: !916, line: 116, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!934 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !935, file: !917, line: 73)
!935 = !DISubprogram(name: "isupper", scope: !916, file: !916, line: 117, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!936 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !937, file: !917, line: 74)
!937 = !DISubprogram(name: "isxdigit", scope: !916, file: !916, line: 118, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!938 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !939, file: !917, line: 75)
!939 = !DISubprogram(name: "tolower", scope: !916, file: !916, line: 122, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!940 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !941, file: !917, line: 76)
!941 = !DISubprogram(name: "toupper", scope: !916, file: !916, line: 125, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!942 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !943, file: !917, line: 87)
!943 = !DISubprogram(name: "isblank", scope: !916, file: !916, line: 130, type: !240, flags: DIFlagPrototyped, spFlags: 0)
!944 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !945, file: !946, line: 44)
!945 = !DIDerivedType(tag: DW_TAG_typedef, name: "size_t", scope: !2, file: !866, line: 258, baseType: !101)
!946 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/ext/new_allocator.h", directory: "")
!947 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !302, entity: !948, file: !946, line: 45)
!948 = !DIDerivedType(tag: DW_TAG_typedef, name: "ptrdiff_t", scope: !2, file: !866, line: 259, baseType: !58)
!949 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !950, file: !954, line: 82)
!950 = !DIDerivedType(tag: DW_TAG_typedef, name: "wctrans_t", file: !951, line: 48, baseType: !952)
!951 = !DIFile(filename: "/usr/include/wctype.h", directory: "")
!952 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !953, size: 64)
!953 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !54)
!954 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/cwctype", directory: "")
!955 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !956, file: !954, line: 83)
!956 = !DIDerivedType(tag: DW_TAG_typedef, name: "wctype_t", file: !957, line: 38, baseType: !101)
!957 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/wctype-wchar.h", directory: "")
!958 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !599, file: !954, line: 84)
!959 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !960, file: !954, line: 86)
!960 = !DISubprogram(name: "iswalnum", scope: !957, file: !957, line: 95, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!961 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !962, file: !954, line: 87)
!962 = !DISubprogram(name: "iswalpha", scope: !957, file: !957, line: 101, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!963 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !964, file: !954, line: 89)
!964 = !DISubprogram(name: "iswblank", scope: !957, file: !957, line: 146, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!965 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !966, file: !954, line: 91)
!966 = !DISubprogram(name: "iswcntrl", scope: !957, file: !957, line: 104, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!967 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !968, file: !954, line: 92)
!968 = !DISubprogram(name: "iswctype", scope: !957, file: !957, line: 159, type: !969, flags: DIFlagPrototyped, spFlags: 0)
!969 = !DISubroutineType(types: !970)
!970 = !{!11, !599, !956}
!971 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !972, file: !954, line: 93)
!972 = !DISubprogram(name: "iswdigit", scope: !957, file: !957, line: 108, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!973 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !974, file: !954, line: 94)
!974 = !DISubprogram(name: "iswgraph", scope: !957, file: !957, line: 112, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!975 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !976, file: !954, line: 95)
!976 = !DISubprogram(name: "iswlower", scope: !957, file: !957, line: 117, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!977 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !978, file: !954, line: 96)
!978 = !DISubprogram(name: "iswprint", scope: !957, file: !957, line: 120, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!979 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !980, file: !954, line: 97)
!980 = !DISubprogram(name: "iswpunct", scope: !957, file: !957, line: 125, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!981 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !982, file: !954, line: 98)
!982 = !DISubprogram(name: "iswspace", scope: !957, file: !957, line: 130, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!983 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !984, file: !954, line: 99)
!984 = !DISubprogram(name: "iswupper", scope: !957, file: !957, line: 135, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!985 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !986, file: !954, line: 100)
!986 = !DISubprogram(name: "iswxdigit", scope: !957, file: !957, line: 140, type: !780, flags: DIFlagPrototyped, spFlags: 0)
!987 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !988, file: !954, line: 101)
!988 = !DISubprogram(name: "towctrans", scope: !951, file: !951, line: 55, type: !989, flags: DIFlagPrototyped, spFlags: 0)
!989 = !DISubroutineType(types: !990)
!990 = !{!599, !599, !950}
!991 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !992, file: !954, line: 102)
!992 = !DISubprogram(name: "towlower", scope: !957, file: !957, line: 166, type: !993, flags: DIFlagPrototyped, spFlags: 0)
!993 = !DISubroutineType(types: !994)
!994 = !{!599, !599}
!995 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !996, file: !954, line: 103)
!996 = !DISubprogram(name: "towupper", scope: !957, file: !957, line: 169, type: !993, flags: DIFlagPrototyped, spFlags: 0)
!997 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !998, file: !954, line: 104)
!998 = !DISubprogram(name: "wctrans", scope: !951, file: !951, line: 52, type: !999, flags: DIFlagPrototyped, spFlags: 0)
!999 = !DISubroutineType(types: !1000)
!1000 = !{!950, !173}
!1001 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !2, entity: !1002, file: !954, line: 105)
!1002 = !DISubprogram(name: "wctype", scope: !957, file: !957, line: 155, type: !1003, flags: DIFlagPrototyped, spFlags: 0)
!1003 = !DISubroutineType(types: !1004)
!1004 = !{!956, !173}
!1005 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !338, file: !1006, line: 38)
!1006 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/stdlib.h", directory: "")
!1007 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !342, file: !1006, line: 39)
!1008 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !376, file: !1006, line: 40)
!1009 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !347, file: !1006, line: 43)
!1010 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !419, file: !1006, line: 46)
!1011 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !328, file: !1006, line: 51)
!1012 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !332, file: !1006, line: 52)
!1013 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !1014, file: !1006, line: 54)
!1014 = !DISubprogram(name: "abs", linkageName: "_ZSt3absg", scope: !2, file: !326, line: 103, type: !1015, flags: DIFlagPrototyped, spFlags: 0)
!1015 = !DISubroutineType(types: !1016)
!1016 = !{!1017, !1017}
!1017 = !DIBasicType(name: "__float128", size: 128, encoding: DW_ATE_float)
!1018 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !349, file: !1006, line: 55)
!1019 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !354, file: !1006, line: 56)
!1020 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !356, file: !1006, line: 57)
!1021 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !360, file: !1006, line: 58)
!1022 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !368, file: !1006, line: 59)
!1023 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !500, file: !1006, line: 60)
!1024 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !380, file: !1006, line: 61)
!1025 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !384, file: !1006, line: 62)
!1026 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !388, file: !1006, line: 63)
!1027 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !392, file: !1006, line: 64)
!1028 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !396, file: !1006, line: 65)
!1029 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !400, file: !1006, line: 67)
!1030 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !404, file: !1006, line: 68)
!1031 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !411, file: !1006, line: 69)
!1032 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !415, file: !1006, line: 71)
!1033 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !421, file: !1006, line: 72)
!1034 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !423, file: !1006, line: 73)
!1035 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !427, file: !1006, line: 74)
!1036 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !431, file: !1006, line: 75)
!1037 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !436, file: !1006, line: 76)
!1038 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !440, file: !1006, line: 77)
!1039 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !444, file: !1006, line: 78)
!1040 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !446, file: !1006, line: 80)
!1041 = !DIImportedEntity(tag: DW_TAG_imported_declaration, scope: !37, entity: !453, file: !1006, line: 81)
!1042 = !DIImportedEntity(tag: DW_TAG_imported_module, scope: !37, entity: !2, file: !31, line: 12)
!1043 = !DICompositeType(tag: DW_TAG_array_type, baseType: !1044, size: 256, elements: !1052)
!1044 = distinct !DICompositeType(tag: DW_TAG_structure_type, name: "option", file: !1045, line: 50, size: 256, flags: DIFlagTypePassByValue, elements: !1046, identifier: "_ZTS6option")
!1045 = !DIFile(filename: "/usr/include/x86_64-linux-gnu/bits/getopt_ext.h", directory: "")
!1046 = !{!1047, !1048, !1049, !1051}
!1047 = !DIDerivedType(tag: DW_TAG_member, name: "name", scope: !1044, file: !1045, line: 52, baseType: !173, size: 64)
!1048 = !DIDerivedType(tag: DW_TAG_member, name: "has_arg", scope: !1044, file: !1045, line: 55, baseType: !11, size: 32, offset: 64)
!1049 = !DIDerivedType(tag: DW_TAG_member, name: "flag", scope: !1044, file: !1045, line: 56, baseType: !1050, size: 64, offset: 128)
!1050 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !11, size: 64)
!1051 = !DIDerivedType(tag: DW_TAG_member, name: "val", scope: !1044, file: !1045, line: 57, baseType: !11, size: 32, offset: 192)
!1052 = !{!1053}
!1053 = !DISubrange(count: 1)
!1054 = !{i32 7, !"Dwarf Version", i32 4}
!1055 = !{i32 2, !"Debug Info Version", i32 3}
!1056 = !{i32 1, !"wchar_size", i32 4}
!1057 = !{!"clang version 12.0.1 (git@github.com:fengzhengzhan/STFGFuzz.git 4ed35f2f97b6ad76c9de46553c4fdd545c0c1eb2)"}
!1058 = distinct !DISubprogram(name: "__cxx_global_var_init", scope: !31, file: !31, type: !339, flags: DIFlagArtificial, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !37, retainedNodes: !38)
!1059 = !DILocation(line: 74, column: 25, scope: !1060)
!1060 = !DILexicalBlockFile(scope: !1058, file: !3, discriminator: 0)
!1061 = !DILocation(line: 0, scope: !1058)
!1062 = distinct !DISubprogram(name: "bug", linkageName: "_Z3bugv", scope: !31, file: !31, line: 14, type: !339, scopeLine: 14, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !37, retainedNodes: !38)
!1063 = !DILocalVariable(name: "i", scope: !1062, file: !31, line: 15, type: !11)
!1064 = !DILocation(line: 15, column: 9, scope: !1062)
!1065 = !DILocalVariable(name: "j", scope: !1062, file: !31, line: 16, type: !11)
!1066 = !DILocation(line: 16, column: 9, scope: !1062)
!1067 = !DILocalVariable(name: "k", scope: !1062, file: !31, line: 17, type: !11)
!1068 = !DILocation(line: 17, column: 9, scope: !1062)
!1069 = !DILocation(line: 18, column: 9, scope: !1062)
!1070 = !DILocation(line: 18, column: 13, scope: !1062)
!1071 = !DILocation(line: 18, column: 11, scope: !1062)
!1072 = !DILocation(line: 18, column: 7, scope: !1062)
!1073 = !DILocation(line: 19, column: 1, scope: !1062)
!1074 = distinct !DISubprogram(name: "bug", linkageName: "_Z3bugi", scope: !31, file: !31, line: 21, type: !377, scopeLine: 21, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !37, retainedNodes: !38)
!1075 = !DILocalVariable(name: "a", arg: 1, scope: !1074, file: !31, line: 21, type: !11)
!1076 = !DILocation(line: 21, column: 14, scope: !1074)
!1077 = !DILocalVariable(name: "i", scope: !1074, file: !31, line: 22, type: !11)
!1078 = !DILocation(line: 22, column: 9, scope: !1074)
!1079 = !DILocalVariable(name: "j", scope: !1074, file: !31, line: 23, type: !11)
!1080 = !DILocation(line: 23, column: 9, scope: !1074)
!1081 = !DILocalVariable(name: "k", scope: !1074, file: !31, line: 24, type: !11)
!1082 = !DILocation(line: 24, column: 9, scope: !1074)
!1083 = !DILocation(line: 25, column: 9, scope: !1074)
!1084 = !DILocation(line: 25, column: 13, scope: !1074)
!1085 = !DILocation(line: 25, column: 11, scope: !1074)
!1086 = !DILocation(line: 25, column: 7, scope: !1074)
!1087 = !DILocation(line: 26, column: 1, scope: !1074)
!1088 = distinct !DISubprogram(name: "bug", linkageName: "_Z3bugNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE", scope: !31, file: !31, line: 28, type: !1089, scopeLine: 28, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !37, retainedNodes: !38)
!1089 = !DISubroutineType(types: !1090)
!1090 = !{null, !1091}
!1091 = !DIDerivedType(tag: DW_TAG_typedef, name: "string", scope: !2, file: !1092, line: 79, baseType: !1093)
!1092 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/stringfwd.h", directory: "")
!1093 = !DICompositeType(tag: DW_TAG_class_type, name: "basic_string<char, std::char_traits<char>, std::allocator<char> >", scope: !1095, file: !1094, line: 1608, size: 256, flags: DIFlagFwdDecl | DIFlagNonTrivial, identifier: "_ZTSNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE")
!1094 = !DIFile(filename: "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/basic_string.tcc", directory: "")
!1095 = !DINamespace(name: "__cxx11", scope: !2, exportSymbols: true)
!1096 = !DILocalVariable(name: "a", arg: 1, scope: !1088, file: !31, line: 28, type: !1091)
!1097 = !DILocation(line: 28, column: 17, scope: !1088)
!1098 = !DILocalVariable(name: "i", scope: !1088, file: !31, line: 29, type: !11)
!1099 = !DILocation(line: 29, column: 9, scope: !1088)
!1100 = !DILocalVariable(name: "j", scope: !1088, file: !31, line: 30, type: !11)
!1101 = !DILocation(line: 30, column: 9, scope: !1088)
!1102 = !DILocalVariable(name: "k", scope: !1088, file: !31, line: 31, type: !11)
!1103 = !DILocation(line: 31, column: 9, scope: !1088)
!1104 = !DILocation(line: 32, column: 9, scope: !1088)
!1105 = !DILocation(line: 32, column: 13, scope: !1088)
!1106 = !DILocation(line: 32, column: 11, scope: !1088)
!1107 = !DILocation(line: 32, column: 7, scope: !1088)
!1108 = !DILocation(line: 33, column: 1, scope: !1088)
!1109 = !DILocalVariable(name: "argc", arg: 1, scope: !30, file: !31, line: 35, type: !11)
!1110 = !DILocation(line: 35, column: 14, scope: !30)
!1111 = !DILocalVariable(name: "argv", arg: 2, scope: !30, file: !31, line: 35, type: !34)
!1112 = !DILocation(line: 35, column: 26, scope: !30)
!1113 = !DILocalVariable(name: "opt", scope: !30, file: !31, line: 37, type: !11)
!1114 = !DILocation(line: 37, column: 9, scope: !30)
!1115 = !DILocalVariable(name: "opt_index", scope: !30, file: !31, line: 37, type: !11)
!1116 = !DILocation(line: 37, column: 14, scope: !30)
!1117 = !DILocalVariable(name: "filename", scope: !30, file: !31, line: 38, type: !35)
!1118 = !DILocation(line: 38, column: 11, scope: !30)
!1119 = !DILocation(line: 43, column: 5, scope: !30)
!1120 = !DILocation(line: 43, column: 30, scope: !30)
!1121 = !DILocation(line: 43, column: 36, scope: !30)
!1122 = !DILocation(line: 43, column: 18, scope: !30)
!1123 = !DILocation(line: 43, column: 16, scope: !30)
!1124 = !DILocation(line: 43, column: 75, scope: !30)
!1125 = !DILocation(line: 45, column: 17, scope: !1126)
!1126 = distinct !DILexicalBlock(scope: !30, file: !31, line: 44, column: 5)
!1127 = !DILocation(line: 45, column: 9, scope: !1126)
!1128 = !DILocation(line: 48, column: 24, scope: !1129)
!1129 = distinct !DILexicalBlock(scope: !1126, file: !31, line: 46, column: 9)
!1130 = !DILocation(line: 48, column: 22, scope: !1129)
!1131 = !DILocation(line: 49, column: 13, scope: !1129)
!1132 = !DILocation(line: 52, column: 13, scope: !1129)
!1133 = !DILocation(line: 53, column: 13, scope: !1129)
!1134 = distinct !{!1134, !1119, !1135, !1136}
!1135 = !DILocation(line: 56, column: 5, scope: !30)
!1136 = !{!"llvm.loop.mustprogress"}
!1137 = !DILocalVariable(name: "str", scope: !30, file: !31, line: 59, type: !1138)
!1138 = !DICompositeType(tag: DW_TAG_array_type, baseType: !36, size: 1608, elements: !1139)
!1139 = !{!1140}
!1140 = !DISubrange(count: 201)
!1141 = !DILocation(line: 59, column: 10, scope: !30)
!1142 = !DILocalVariable(name: "fp", scope: !30, file: !31, line: 60, type: !143)
!1143 = !DILocation(line: 60, column: 11, scope: !30)
!1144 = !DILocation(line: 60, column: 22, scope: !30)
!1145 = !DILocation(line: 60, column: 16, scope: !30)
!1146 = !DILocation(line: 61, column: 11, scope: !30)
!1147 = !DILocation(line: 61, column: 19, scope: !30)
!1148 = !DILocation(line: 61, column: 5, scope: !30)
!1149 = !DILocalVariable(name: "buffer", scope: !30, file: !31, line: 65, type: !1150)
!1150 = !DICompositeType(tag: DW_TAG_array_type, baseType: !36, size: 360, elements: !1151)
!1151 = !{!1152}
!1152 = !DISubrange(count: 45)
!1153 = !DILocation(line: 65, column: 10, scope: !30)
!1154 = !DILocation(line: 66, column: 5, scope: !30)
!1155 = !DILocation(line: 68, column: 5, scope: !30)
!1156 = !DILocation(line: 68, column: 16, scope: !30)
!1157 = !DILocation(line: 73, column: 17, scope: !1158)
!1158 = distinct !DILexicalBlock(scope: !30, file: !31, line: 73, column: 9)
!1159 = !DILocation(line: 73, column: 9, scope: !1158)
!1160 = !DILocation(line: 73, column: 56, scope: !1158)
!1161 = !DILocation(line: 73, column: 61, scope: !1158)
!1162 = !DILocation(line: 74, column: 18, scope: !1158)
!1163 = !DILocation(line: 74, column: 9, scope: !1158)
!1164 = !DILocation(line: 74, column: 49, scope: !1158)
!1165 = !DILocation(line: 74, column: 54, scope: !1158)
!1166 = !DILocation(line: 75, column: 17, scope: !1158)
!1167 = !DILocation(line: 75, column: 9, scope: !1158)
!1168 = !DILocation(line: 75, column: 46, scope: !1158)
!1169 = !DILocation(line: 73, column: 9, scope: !30)
!1170 = !DILocation(line: 76, column: 5, scope: !1171)
!1171 = distinct !DILexicalBlock(scope: !1158, file: !31, line: 75, column: 52)
!1172 = !DILocation(line: 79, column: 5, scope: !30)
!1173 = !DILocalVariable(name: "s1", scope: !30, file: !31, line: 81, type: !1138)
!1174 = !DILocation(line: 81, column: 10, scope: !30)
!1175 = !DILocalVariable(name: "s2", scope: !30, file: !31, line: 81, type: !1138)
!1176 = !DILocation(line: 81, column: 17, scope: !30)
!1177 = !DILocalVariable(name: "s3", scope: !30, file: !31, line: 81, type: !1138)
!1178 = !DILocation(line: 81, column: 24, scope: !30)
!1179 = !DILocalVariable(name: "i", scope: !1180, file: !31, line: 82, type: !11)
!1180 = distinct !DILexicalBlock(scope: !30, file: !31, line: 82, column: 5)
!1181 = !DILocation(line: 82, column: 14, scope: !1180)
!1182 = !DILocation(line: 82, column: 10, scope: !1180)
!1183 = !DILocation(line: 82, column: 21, scope: !1184)
!1184 = distinct !DILexicalBlock(scope: !1180, file: !31, line: 82, column: 5)
!1185 = !DILocation(line: 82, column: 23, scope: !1184)
!1186 = !DILocation(line: 82, column: 5, scope: !1180)
!1187 = !DILocation(line: 83, column: 21, scope: !1188)
!1188 = distinct !DILexicalBlock(scope: !1184, file: !31, line: 82, column: 35)
!1189 = !DILocation(line: 83, column: 22, scope: !1188)
!1190 = !DILocation(line: 83, column: 17, scope: !1188)
!1191 = !DILocation(line: 83, column: 12, scope: !1188)
!1192 = !DILocation(line: 83, column: 9, scope: !1188)
!1193 = !DILocation(line: 83, column: 15, scope: !1188)
!1194 = !DILocation(line: 84, column: 5, scope: !1188)
!1195 = !DILocation(line: 82, column: 31, scope: !1184)
!1196 = !DILocation(line: 82, column: 5, scope: !1184)
!1197 = distinct !{!1197, !1186, !1198, !1136}
!1198 = !DILocation(line: 84, column: 5, scope: !1180)
!1199 = !DILocation(line: 85, column: 5, scope: !30)
!1200 = !DILocation(line: 85, column: 11, scope: !30)
!1201 = !DILocalVariable(name: "i", scope: !1202, file: !31, line: 86, type: !11)
!1202 = distinct !DILexicalBlock(scope: !30, file: !31, line: 86, column: 5)
!1203 = !DILocation(line: 86, column: 14, scope: !1202)
!1204 = !DILocation(line: 86, column: 10, scope: !1202)
!1205 = !DILocation(line: 86, column: 21, scope: !1206)
!1206 = distinct !DILexicalBlock(scope: !1202, file: !31, line: 86, column: 5)
!1207 = !DILocation(line: 86, column: 23, scope: !1206)
!1208 = !DILocation(line: 86, column: 5, scope: !1202)
!1209 = !DILocation(line: 87, column: 21, scope: !1210)
!1210 = distinct !DILexicalBlock(scope: !1206, file: !31, line: 86, column: 34)
!1211 = !DILocation(line: 87, column: 22, scope: !1210)
!1212 = !DILocation(line: 87, column: 30, scope: !1210)
!1213 = !DILocation(line: 87, column: 17, scope: !1210)
!1214 = !DILocation(line: 87, column: 12, scope: !1210)
!1215 = !DILocation(line: 87, column: 9, scope: !1210)
!1216 = !DILocation(line: 87, column: 15, scope: !1210)
!1217 = !DILocation(line: 88, column: 5, scope: !1210)
!1218 = !DILocation(line: 86, column: 30, scope: !1206)
!1219 = !DILocation(line: 86, column: 5, scope: !1206)
!1220 = distinct !{!1220, !1208, !1221, !1136}
!1221 = !DILocation(line: 88, column: 5, scope: !1202)
!1222 = !DILocation(line: 89, column: 5, scope: !30)
!1223 = !DILocation(line: 89, column: 10, scope: !30)
!1224 = !DILocalVariable(name: "i", scope: !1225, file: !31, line: 90, type: !11)
!1225 = distinct !DILexicalBlock(scope: !30, file: !31, line: 90, column: 5)
!1226 = !DILocation(line: 90, column: 14, scope: !1225)
!1227 = !DILocation(line: 90, column: 10, scope: !1225)
!1228 = !DILocation(line: 90, column: 21, scope: !1229)
!1229 = distinct !DILexicalBlock(scope: !1225, file: !31, line: 90, column: 5)
!1230 = !DILocation(line: 90, column: 23, scope: !1229)
!1231 = !DILocation(line: 90, column: 5, scope: !1225)
!1232 = !DILocation(line: 91, column: 21, scope: !1233)
!1233 = distinct !DILexicalBlock(scope: !1229, file: !31, line: 90, column: 34)
!1234 = !DILocation(line: 91, column: 22, scope: !1233)
!1235 = !DILocation(line: 91, column: 30, scope: !1233)
!1236 = !DILocation(line: 91, column: 33, scope: !1233)
!1237 = !DILocation(line: 91, column: 17, scope: !1233)
!1238 = !DILocation(line: 91, column: 12, scope: !1233)
!1239 = !DILocation(line: 91, column: 9, scope: !1233)
!1240 = !DILocation(line: 91, column: 15, scope: !1233)
!1241 = !DILocation(line: 92, column: 5, scope: !1233)
!1242 = !DILocation(line: 90, column: 30, scope: !1229)
!1243 = !DILocation(line: 90, column: 5, scope: !1229)
!1244 = distinct !{!1244, !1231, !1245, !1136}
!1245 = !DILocation(line: 92, column: 5, scope: !1225)
!1246 = !DILocation(line: 93, column: 5, scope: !30)
!1247 = !DILocation(line: 93, column: 10, scope: !30)
!1248 = !DILocation(line: 94, column: 20, scope: !30)
!1249 = !DILocation(line: 94, column: 5, scope: !30)
!1250 = !DILocalVariable(name: "x", scope: !30, file: !31, line: 96, type: !99)
!1251 = !DILocation(line: 96, column: 14, scope: !30)
!1252 = !DILocation(line: 96, column: 27, scope: !30)
!1253 = !DILocation(line: 96, column: 18, scope: !30)
!1254 = !DILocation(line: 97, column: 9, scope: !1255)
!1255 = distinct !DILexicalBlock(scope: !30, file: !31, line: 97, column: 9)
!1256 = !DILocation(line: 97, column: 11, scope: !1255)
!1257 = !DILocation(line: 97, column: 9, scope: !30)
!1258 = !DILocation(line: 98, column: 9, scope: !1259)
!1259 = distinct !DILexicalBlock(scope: !1255, file: !31, line: 97, column: 34)
!1260 = !DILocalVariable(name: "y", scope: !30, file: !31, line: 101, type: !95)
!1261 = !DILocation(line: 101, column: 14, scope: !30)
!1262 = !DILocation(line: 101, column: 26, scope: !30)
!1263 = !DILocation(line: 101, column: 18, scope: !30)
!1264 = !DILocation(line: 102, column: 9, scope: !1265)
!1265 = distinct !DILexicalBlock(scope: !30, file: !31, line: 102, column: 9)
!1266 = !DILocation(line: 102, column: 11, scope: !1265)
!1267 = !DILocation(line: 102, column: 9, scope: !30)
!1268 = !DILocation(line: 103, column: 9, scope: !1269)
!1269 = distinct !DILexicalBlock(scope: !1265, file: !31, line: 102, column: 26)
!1270 = !DILocalVariable(name: "z", scope: !30, file: !31, line: 106, type: !91)
!1271 = !DILocation(line: 106, column: 14, scope: !30)
!1272 = !DILocation(line: 106, column: 26, scope: !30)
!1273 = !DILocation(line: 106, column: 18, scope: !30)
!1274 = !DILocation(line: 108, column: 13, scope: !30)
!1275 = !DILocation(line: 108, column: 5, scope: !30)
!1276 = !DILocation(line: 110, column: 9, scope: !1277)
!1277 = distinct !DILexicalBlock(scope: !30, file: !31, line: 108, column: 16)
!1278 = !DILocation(line: 113, column: 9, scope: !1277)
!1279 = !DILocation(line: 116, column: 9, scope: !1277)
!1280 = !DILocation(line: 119, column: 9, scope: !1277)
!1281 = !DILocation(line: 122, column: 5, scope: !30)
!1282 = !DILocation(line: 123, column: 5, scope: !30)
!1283 = !DILocation(line: 124, column: 9, scope: !30)
!1284 = !DILocation(line: 124, column: 5, scope: !30)
!1285 = !DILocation(line: 125, column: 5, scope: !30)
!1286 = !DILocation(line: 127, column: 5, scope: !30)
!1287 = !DILocation(line: 128, column: 1, scope: !30)
!1288 = distinct !DISubprogram(linkageName: "_GLOBAL__sub_I_demo.cc", scope: !31, file: !31, type: !1289, flags: DIFlagArtificial, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !37, retainedNodes: !38)
!1289 = !DISubroutineType(types: !38)
!1290 = !DILocation(line: 0, scope: !1288)

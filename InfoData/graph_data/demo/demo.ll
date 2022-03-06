; ModuleID = 'demo/demo.cc'
source_filename = "demo/demo.cc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%"class.std::ios_base::Init" = type { i8 }
%struct.option = type { i8*, i32, i32*, i32 }
%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque

$"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f" = comdat any

$main = comdat any

$"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f" = comdat any

$sancov.module_ctor_trace_pc_guard = comdat any

@_ZStL8__ioinit = internal global { %"class.std::ios_base::Init", [63 x i8] } zeroinitializer, align 32
@__dso_handle = external hidden global i8
@_ZZ4mainE12long_options = internal global { [1 x %struct.option], [32 x i8] } { [1 x %struct.option] [%struct.option { i8* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0, i32 0), i32 1, i32* null, i32 102 }], [32 x i8] zeroinitializer }, align 32
@.str = internal constant { [5 x i8], [59 x i8] } { [5 x i8] c"file\00", [59 x i8] zeroinitializer }, align 32
@.str.1 = internal constant { [3 x i8], [61 x i8] } { [3 x i8] c"f:\00", [61 x i8] zeroinitializer }, align 32
@optarg = external dso_local global i8*, align 8
@.str.2 = internal constant { [18 x i8], [46 x i8] } { [18 x i8] c"Error Parameters!\00", [46 x i8] zeroinitializer }, align 32
@.str.3 = internal constant { [2 x i8], [62 x i8] } { [2 x i8] c"r\00", [62 x i8] zeroinitializer }, align 32
@.str.4 = internal constant { [21 x i8], [43 x i8] } { [21 x i8] c"The quick brown fox \00", [43 x i8] zeroinitializer }, align 32
@.str.5 = internal constant { [12 x i8], [52 x i8] } { [12 x i8] c"jumps over \00", [52 x i8] zeroinitializer }, align 32
@.str.6 = internal constant { [14 x i8], [50 x i8] } { [14 x i8] c"the lazy dog.\00", [50 x i8] zeroinitializer }, align 32
@.str.7 = internal constant { [27 x i8], [37 x i8] } { [27 x i8] c"Though first str/mem Cmp.\0A\00", [37 x i8] zeroinitializer }, align 32
@.str.8 = internal constant { [4 x i8], [60 x i8] } { [4 x i8] c"%s\0A\00", [60 x i8] zeroinitializer }, align 32
@.str.9 = internal constant { [33 x i8], [63 x i8] } { [33 x i8] c"Puzzle solved, Congratulations!\0A\00", [63 x i8] zeroinitializer }, align 32
@__sancov_lowest_stack = external thread_local(initialexec) global i64
@__sancov_gen_ = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !0
@__sancov_gen_.10 = private global [15 x i32] zeroinitializer, section "__sancov_guards", comdat($main), align 4, !associated !1
@__sancov_gen_cov_switch_values = internal global [3 x i64] [i64 1, i64 32, i64 102]
@__sancov_gen_cov_switch_values.11 = internal global [5 x i64] [i64 3, i64 32, i64 48879, i64 61374, i64 65259]
@__sancov_gen_.12 = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !2
@__start___sancov_guards = external hidden global i32
@__stop___sancov_guards = external hidden global i32
@__asan_option_detect_stack_use_after_return = external global i32
@___asan_gen_ = private unnamed_addr constant [87 x i8] c"6 32 4 9 opt_index 48 201 3 str 320 45 6 buffer 400 201 2 s1 672 201 2 s2 944 201 2 s3\00", align 1
@___asan_gen_.13 = private constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.14 = private unnamed_addr constant [14 x i8] c"std::__ioinit\00", align 1
@___asan_gen_.15 = private unnamed_addr constant [67 x i8] c"/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream\00", align 1
@___asan_gen_.16 = private unnamed_addr constant { [67 x i8]*, i32, i32 } { [67 x i8]* @___asan_gen_.15, i32 74, i32 25 }
@___asan_gen_.17 = private unnamed_addr constant [13 x i8] c"long_options\00", align 1
@___asan_gen_.18 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.19 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.18, i32 18, i32 26 }
@___asan_gen_.20 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.21 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.22 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.21, i32 20, i32 10 }
@___asan_gen_.23 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.24 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.25 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.24, i32 22, i32 42 }
@___asan_gen_.26 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.27 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.28 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.27, i32 31, i32 20 }
@___asan_gen_.29 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.30 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.31 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.30, i32 39, i32 32 }
@___asan_gen_.32 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.33 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.34 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.33, i32 52, i32 28 }
@___asan_gen_.35 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.36 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.37 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.36, i32 53, i32 30 }
@___asan_gen_.38 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.39 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.40 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.39, i32 54, i32 29 }
@___asan_gen_.41 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.42 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.43 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.42, i32 58, i32 12 }
@___asan_gen_.44 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.45 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.46 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.45, i32 73, i32 12 }
@___asan_gen_.47 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.48 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.49 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.48, i32 101, i32 12 }
@llvm.compiler.used = appending global [15 x i8*] [i8* bitcast ([1 x i32]* @__sancov_gen_ to i8*), i8* bitcast ([15 x i32]* @__sancov_gen_.10 to i8*), i8* bitcast ([1 x i32]* @__sancov_gen_.12 to i8*), i8* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0, i32 0), i8* bitcast ({ [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options to i8*), i8* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.4, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.5, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.6, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.7, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.8, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.9, i32 0, i32 0, i32 0)], section "llvm.metadata"
@0 = internal global [12 x { i64, i64, i64, i64, i64, i64, i64, i64 }] [{ i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit to i64), i64 1, i64 64, i64 ptrtoint ([14 x i8]* @___asan_gen_.14 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 1, i64 ptrtoint ({ [67 x i8]*, i32, i32 }* @___asan_gen_.16 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options to i64), i64 32, i64 64, i64 ptrtoint ([13 x i8]* @___asan_gen_.17 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.19 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [5 x i8], [59 x i8] }* @.str to i64), i64 5, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.20 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.22 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [3 x i8], [61 x i8] }* @.str.1 to i64), i64 3, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.23 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.25 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [18 x i8], [46 x i8] }* @.str.2 to i64), i64 18, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.26 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.28 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [2 x i8], [62 x i8] }* @.str.3 to i64), i64 2, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.29 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.31 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [21 x i8], [43 x i8] }* @.str.4 to i64), i64 21, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.32 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.34 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [12 x i8], [52 x i8] }* @.str.5 to i64), i64 12, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.35 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.37 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [14 x i8], [50 x i8] }* @.str.6 to i64), i64 14, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.38 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.40 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [27 x i8], [37 x i8] }* @.str.7 to i64), i64 27, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.41 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.43 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [4 x i8], [60 x i8] }* @.str.8 to i64), i64 4, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.44 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.46 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [33 x i8], [63 x i8] }* @.str.9 to i64), i64 33, i64 96, i64 ptrtoint ([17 x i8]* @___asan_gen_.47 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.49 to i64), i64 -1 }]
@llvm.global_ctors = appending global [3 x { i32, void ()*, i8* }] [{ i32, void ()*, i8* } { i32 65535, void ()* @_GLOBAL__sub_I_demo.cc, i8* null }, { i32, void ()*, i8* } { i32 2, void ()* @sancov.module_ctor_trace_pc_guard, i8* bitcast (void ()* @sancov.module_ctor_trace_pc_guard to i8*) }, { i32, void ()*, i8* } { i32 1, void ()* @asan.module_ctor, i8* null }]
@llvm.global_dtors = appending global [1 x { i32, void ()*, i8* }] [{ i32, void ()*, i8* } { i32 1, void ()* @asan.module_dtor, i8* null }]

; Function Attrs: noinline sanitize_address uwtable
define internal void @__cxx_global_var_init() #0 section ".text.startup" comdat($"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f") {
entry:
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([1 x i32], [1 x i32]* @__sancov_gen_, i32 0, i32 0)) #8
  call void @_ZNSt8ios_base4InitC1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1) getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0))
  %0 = call i32 @__cxa_atexit(void (i8*)* bitcast (void (%"class.std::ios_base::Init"*)* @_ZNSt8ios_base4InitD1Ev to void (i8*)*), i8* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0, i32 0), i8* @__dso_handle) #3
  ret void
}

declare dso_local void @_ZNSt8ios_base4InitC1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1)) unnamed_addr #1

; Function Attrs: nounwind
declare dso_local void @_ZNSt8ios_base4InitD1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1)) unnamed_addr #2

; Function Attrs: nounwind
declare dso_local i32 @__cxa_atexit(void (i8*)*, i8*, i8*) #3

; Function Attrs: noinline norecurse optnone sanitize_address uwtable mustprogress
define dso_local i32 @main(i32 %argc, i8** %argv) #4 comdat {
entry:
  %retval = alloca i32, align 4
  %argc.addr = alloca i32, align 4
  %argv.addr = alloca i8**, align 8
  %opt = alloca i32, align 4
  %filename = alloca i8*, align 8
  %fp = alloca %struct._IO_FILE*, align 8
  %cleanup.dest.slot = alloca i32, align 4
  %i = alloca i32, align 4
  %i22 = alloca i32, align 4
  %i37 = alloca i32, align 4
  %x = alloca i64, align 8
  %y = alloca i32, align 4
  %z = alloca i16, align 2
  %asan_local_stack_base = alloca i64, align 8
  %0 = load i32, i32* @__asan_option_detect_stack_use_after_return, align 4
  %1 = icmp ne i32 %0, 0
  br i1 %1, label %2, label %4

2:                                                ; preds = %entry
  %3 = call i64 @__asan_stack_malloc_5(i64 1216)
  br label %4

4:                                                ; preds = %entry, %2
  %5 = phi i64 [ 0, %entry ], [ %3, %2 ]
  %6 = icmp eq i64 %5, 0
  br i1 %6, label %7, label %9

7:                                                ; preds = %4
  %MyAlloca = alloca i8, i64 1216, align 32
  %8 = ptrtoint i8* %MyAlloca to i64
  br label %9

9:                                                ; preds = %4, %7
  %10 = phi i64 [ %5, %4 ], [ %8, %7 ]
  store i64 %10, i64* %asan_local_stack_base, align 8
  %11 = add i64 %10, 32
  %12 = inttoptr i64 %11 to i32*
  %13 = add i64 %10, 48
  %14 = inttoptr i64 %13 to [201 x i8]*
  %15 = add i64 %10, 320
  %16 = inttoptr i64 %15 to [45 x i8]*
  %17 = add i64 %10, 400
  %18 = inttoptr i64 %17 to [201 x i8]*
  %19 = add i64 %10, 672
  %20 = inttoptr i64 %19 to [201 x i8]*
  %21 = add i64 %10, 944
  %22 = inttoptr i64 %21 to [201 x i8]*
  %23 = inttoptr i64 %10 to i64*
  store i64 1102416563, i64* %23, align 8
  %24 = add i64 %10, 8
  %25 = inttoptr i64 %24 to i64*
  store i64 ptrtoint ([87 x i8]* @___asan_gen_ to i64), i64* %25, align 8
  %26 = add i64 %10, 16
  %27 = inttoptr i64 %26 to i64*
  store i64 ptrtoint (i32 (i32, i8**)* @main to i64), i64* %27, align 8
  %28 = lshr i64 %10, 3
  %29 = add i64 %28, 2147450880
  %30 = add i64 %29, 0
  %31 = inttoptr i64 %30 to i64*
  store i64 -506387807054204431, i64* %31, align 1
  %32 = add i64 %29, 8
  %33 = inttoptr i64 %32 to i64*
  store i64 -506381209866536712, i64* %33, align 1
  %34 = add i64 %29, 16
  %35 = inttoptr i64 %34 to i64*
  store i64 -506381209866536712, i64* %35, align 1
  %36 = add i64 %29, 24
  %37 = inttoptr i64 %36 to i64*
  store i64 -506381209866536712, i64* %37, align 1
  %38 = add i64 %29, 32
  %39 = inttoptr i64 %38 to i64*
  store i64 -940422246894996750, i64* %39, align 1
  %40 = add i64 %29, 40
  %41 = inttoptr i64 %40 to i64*
  store i64 -940415623954368264, i64* %41, align 1
  %42 = add i64 %29, 48
  %43 = inttoptr i64 %42 to i64*
  store i64 -506381209866538254, i64* %43, align 1
  %44 = add i64 %29, 56
  %45 = inttoptr i64 %44 to i64*
  store i64 -506381209866536712, i64* %45, align 1
  %46 = add i64 %29, 64
  %47 = inttoptr i64 %46 to i64*
  store i64 -506381209866536712, i64* %47, align 1
  %48 = add i64 %29, 72
  %49 = inttoptr i64 %48 to i64*
  store i64 -940422246793938696, i64* %49, align 1
  %50 = add i64 %29, 80
  %51 = inttoptr i64 %50 to i64*
  store i64 -506381209967594766, i64* %51, align 1
  %52 = add i64 %29, 88
  %53 = inttoptr i64 %52 to i64*
  store i64 -506381209866536712, i64* %53, align 1
  %54 = add i64 %29, 96
  %55 = inttoptr i64 %54 to i64*
  store i64 -506381209866536712, i64* %55, align 1
  %56 = add i64 %29, 104
  %57 = inttoptr i64 %56 to i64*
  store i64 -940415623954368264, i64* %57, align 1
  %58 = add i64 %29, 112
  %59 = inttoptr i64 %58 to i64*
  store i64 -506387832807165198, i64* %59, align 1
  %60 = add i64 %29, 120
  %61 = inttoptr i64 %60 to i64*
  store i64 -506381209866536712, i64* %61, align 1
  %62 = add i64 %29, 128
  %63 = inttoptr i64 %62 to i64*
  store i64 -506381209866536712, i64* %63, align 1
  %64 = add i64 %29, 136
  %65 = inttoptr i64 %64 to i64*
  store i64 -506381209866536712, i64* %65, align 1
  %66 = add i64 %29, 144
  %67 = inttoptr i64 %66 to i64*
  store i64 -868082074056920077, i64* %67, align 1
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([15 x i32], [15 x i32]* @__sancov_gen_.10, i32 0, i32 0)) #8
  store i32 0, i32* %retval, align 4
  store i32 %argc, i32* %argc.addr, align 4
  store i8** %argv, i8*** %argv.addr, align 8
  %68 = bitcast i32* %opt to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %68) #3
  %69 = bitcast i32* %12 to i8*
  %70 = add i64 %29, 4
  %71 = inttoptr i64 %70 to i8*
  store i8 4, i8* %71, align 1
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %69) #3
  %72 = bitcast i8** %filename to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %72) #3
  br label %while.cond

while.cond:                                       ; preds = %sw.epilog, %9
  %73 = load i32, i32* %argc.addr, align 4
  %74 = load i8**, i8*** %argv.addr, align 8
  %call = call i32 @getopt_long(i32 %73, i8** %74, i8* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0, i64 0), %struct.option* getelementptr inbounds ({ [1 x %struct.option], [32 x i8] }, { [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options, i32 0, i32 0, i64 0), i32* %12) #3
  store i32 %call, i32* %opt, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 -1, i32 %call)
  %cmp = icmp ne i32 %call, -1
  br i1 %cmp, label %while.body, label %while.end

while.body:                                       ; preds = %while.cond
  %75 = load i32, i32* %opt, align 4
  %76 = zext i32 %75 to i64
  call void @__sanitizer_cov_trace_switch(i64 %76, i64* getelementptr inbounds ([3 x i64], [3 x i64]* @__sancov_gen_cov_switch_values, i32 0, i32 0))
  switch i32 %75, label %sw.default [
    i32 102, label %sw.bb
  ]

sw.bb:                                            ; preds = %while.body
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 4) to i32*)) #8
  %77 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (i8** @optarg to i64), i64 3), i64 2147450880) to i8*), align 1
  %78 = icmp ne i8 %77, 0
  br i1 %78, label %79, label %80

79:                                               ; preds = %sw.bb
  call void @__asan_report_load8(i64 ptrtoint (i8** @optarg to i64)) #8
  unreachable

80:                                               ; preds = %sw.bb
  %81 = load i8*, i8** @optarg, align 8
  store i8* %81, i8** %filename, align 8
  br label %sw.epilog

sw.default:                                       ; preds = %while.body
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 8) to i32*)) #8
  %call1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0, i64 0))
  br label %sw.epilog

sw.epilog:                                        ; preds = %sw.default, %80
  br label %while.cond, !llvm.loop !29

while.end:                                        ; preds = %while.cond
  %82 = bitcast [201 x i8]* %14 to i8*
  %83 = add i64 %29, 6
  %84 = inttoptr i64 %83 to i64*
  store i64 0, i64* %84, align 1
  %85 = add i64 %29, 14
  %86 = inttoptr i64 %85 to i64*
  store i64 0, i64* %86, align 1
  %87 = add i64 %29, 22
  %88 = inttoptr i64 %87 to i64*
  store i64 0, i64* %88, align 1
  %89 = add i64 %29, 30
  %90 = inttoptr i64 %89 to i16*
  store i16 256, i16* %90, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %82) #3
  %91 = bitcast %struct._IO_FILE** %fp to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %91) #3
  %92 = load i8*, i8** %filename, align 8
  %call2 = call %struct._IO_FILE* @fopen(i8* %92, i8* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0, i64 0))
  store %struct._IO_FILE* %call2, %struct._IO_FILE** %fp, align 8
  %arraydecay = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 0
  %93 = load %struct._IO_FILE*, %struct._IO_FILE** %fp, align 8
  %call3 = call i8* @fgets(i8* %arraydecay, i32 201, %struct._IO_FILE* %93)
  %94 = bitcast [45 x i8]* %16 to i8*
  %95 = add i64 %29, 40
  %96 = inttoptr i64 %95 to i32*
  store i32 0, i32* %96, align 1
  %97 = add i64 %29, 44
  %98 = inttoptr i64 %97 to i16*
  store i16 1280, i16* %98, align 1
  call void @llvm.lifetime.start.p0i8(i64 45, i8* %94) #3
  %99 = bitcast [45 x i8]* %16 to i8*
  %100 = call i8* @__asan_memset(i8* %99, i32 0, i64 45)
  %arraydecay4 = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 0
  %arraydecay5 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 0
  %101 = call i8* @__asan_memcpy(i8* %arraydecay4, i8* %arraydecay5, i64 44)
  %arrayidx = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 44
  %102 = ptrtoint i8* %arrayidx to i64
  %103 = lshr i64 %102, 3
  %104 = add i64 %103, 2147450880
  %105 = inttoptr i64 %104 to i8*
  %106 = load i8, i8* %105, align 1
  %107 = icmp ne i8 %106, 0
  br i1 %107, label %108, label %113, !prof !31

108:                                              ; preds = %while.end
  %109 = and i64 %102, 7
  %110 = trunc i64 %109 to i8
  %111 = icmp sge i8 %110, %106
  br i1 %111, label %112, label %113

112:                                              ; preds = %108
  call void @__asan_report_store1(i64 %102) #8
  unreachable

113:                                              ; preds = %108, %while.end
  store i8 0, i8* %arrayidx, align 4
  %arrayidx6 = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 0
  %call7 = call i32 @memcmp(i8* %arrayidx6, i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.4, i32 0, i32 0, i64 0), i64 20) #9
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call7)
  %cmp8 = icmp ne i32 %call7, 0
  br i1 %cmp8, label %while.end.if.then_crit_edge, label %lor.lhs.false

while.end.if.then_crit_edge:                      ; preds = %113
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 12) to i32*)) #8
  br label %if.then

lor.lhs.false:                                    ; preds = %113
  %arrayidx9 = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 20
  %call10 = call i32 @strncmp(i8* %arrayidx9, i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.5, i32 0, i32 0, i64 0), i64 11) #10
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call10)
  %cmp11 = icmp ne i32 %call10, 0
  br i1 %cmp11, label %lor.lhs.false.if.then_crit_edge, label %lor.lhs.false12

lor.lhs.false.if.then_crit_edge:                  ; preds = %lor.lhs.false
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 16) to i32*)) #8
  br label %if.then

lor.lhs.false12:                                  ; preds = %lor.lhs.false
  %arrayidx13 = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 31
  %call14 = call i32 @strcmp(i8* %arrayidx13, i8* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.6, i32 0, i32 0, i64 0)) #9
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call14)
  %cmp15 = icmp ne i32 %call14, 0
  br i1 %cmp15, label %lor.lhs.false12.if.then_crit_edge, label %if.end

lor.lhs.false12.if.then_crit_edge:                ; preds = %lor.lhs.false12
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 20) to i32*)) #8
  br label %if.then

if.then:                                          ; preds = %lor.lhs.false12.if.then_crit_edge, %lor.lhs.false.if.then_crit_edge, %while.end.if.then_crit_edge
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup80

if.end:                                           ; preds = %lor.lhs.false12
  %call16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.7, i32 0, i32 0, i64 0))
  %114 = bitcast [201 x i8]* %18 to i8*
  %115 = add i64 %29, 50
  %116 = inttoptr i64 %115 to i64*
  store i64 0, i64* %116, align 1
  %117 = add i64 %29, 58
  %118 = inttoptr i64 %117 to i64*
  store i64 0, i64* %118, align 1
  %119 = add i64 %29, 66
  %120 = inttoptr i64 %119 to i64*
  store i64 0, i64* %120, align 1
  %121 = add i64 %29, 74
  %122 = inttoptr i64 %121 to i16*
  store i16 256, i16* %122, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %114) #3
  %123 = bitcast [201 x i8]* %20 to i8*
  %124 = add i64 %29, 84
  %125 = inttoptr i64 %124 to i64*
  store i64 0, i64* %125, align 1
  %126 = add i64 %29, 92
  %127 = inttoptr i64 %126 to i64*
  store i64 0, i64* %127, align 1
  %128 = add i64 %29, 100
  %129 = inttoptr i64 %128 to i64*
  store i64 0, i64* %129, align 1
  %130 = add i64 %29, 108
  %131 = inttoptr i64 %130 to i16*
  store i16 256, i16* %131, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %123) #3
  %132 = bitcast [201 x i8]* %22 to i8*
  %133 = add i64 %29, 118
  %134 = inttoptr i64 %133 to i64*
  store i64 0, i64* %134, align 1
  %135 = add i64 %29, 126
  %136 = inttoptr i64 %135 to i64*
  store i64 0, i64* %136, align 1
  %137 = add i64 %29, 134
  %138 = inttoptr i64 %137 to i64*
  store i64 0, i64* %138, align 1
  %139 = add i64 %29, 142
  %140 = inttoptr i64 %139 to i16*
  store i16 256, i16* %140, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %132) #3
  %141 = bitcast i32* %i to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %141) #3
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %if.end
  %142 = load i32, i32* %i, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 16, i32 %142)
  %cmp17 = icmp slt i32 %142, 16
  br i1 %cmp17, label %for.body, label %for.cond.cleanup

for.cond.cleanup:                                 ; preds = %for.cond
  store i32 5, i32* %cleanup.dest.slot, align 4
  %143 = bitcast i32* %i to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %143) #3
  br label %for.end

for.body:                                         ; preds = %for.cond
  %144 = load i32, i32* %i, align 4
  %add = add nsw i32 %144, 44
  %idxprom = sext i32 %add to i64
  %arrayidx18 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 %idxprom
  %145 = ptrtoint i8* %arrayidx18 to i64
  %146 = lshr i64 %145, 3
  %147 = add i64 %146, 2147450880
  %148 = inttoptr i64 %147 to i8*
  %149 = load i8, i8* %148, align 1
  %150 = icmp ne i8 %149, 0
  br i1 %150, label %151, label %156, !prof !31

151:                                              ; preds = %for.body
  %152 = and i64 %145, 7
  %153 = trunc i64 %152 to i8
  %154 = icmp sge i8 %153, %149
  br i1 %154, label %155, label %156

155:                                              ; preds = %151
  call void @__asan_report_load1(i64 %145) #8
  unreachable

156:                                              ; preds = %151, %for.body
  %157 = load i8, i8* %arrayidx18, align 1
  %158 = load i32, i32* %i, align 4
  %idxprom19 = sext i32 %158 to i64
  %arrayidx20 = getelementptr inbounds [201 x i8], [201 x i8]* %18, i64 0, i64 %idxprom19
  %159 = ptrtoint i8* %arrayidx20 to i64
  %160 = lshr i64 %159, 3
  %161 = add i64 %160, 2147450880
  %162 = inttoptr i64 %161 to i8*
  %163 = load i8, i8* %162, align 1
  %164 = icmp ne i8 %163, 0
  br i1 %164, label %165, label %170, !prof !31

165:                                              ; preds = %156
  %166 = and i64 %159, 7
  %167 = trunc i64 %166 to i8
  %168 = icmp sge i8 %167, %163
  br i1 %168, label %169, label %170

169:                                              ; preds = %165
  call void @__asan_report_store1(i64 %159) #8
  unreachable

170:                                              ; preds = %165, %156
  store i8 %157, i8* %arrayidx20, align 1
  br label %for.inc

for.inc:                                          ; preds = %170
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 24) to i32*)) #8
  %171 = load i32, i32* %i, align 4
  %inc = add nsw i32 %171, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond, !llvm.loop !32

for.end:                                          ; preds = %for.cond.cleanup
  %arrayidx21 = getelementptr inbounds [201 x i8], [201 x i8]* %18, i64 0, i64 16
  %172 = ptrtoint i8* %arrayidx21 to i64
  %173 = lshr i64 %172, 3
  %174 = add i64 %173, 2147450880
  %175 = inttoptr i64 %174 to i8*
  %176 = load i8, i8* %175, align 1
  %177 = icmp ne i8 %176, 0
  br i1 %177, label %178, label %183, !prof !31

178:                                              ; preds = %for.end
  %179 = and i64 %172, 7
  %180 = trunc i64 %179 to i8
  %181 = icmp sge i8 %180, %176
  br i1 %181, label %182, label %183

182:                                              ; preds = %178
  call void @__asan_report_store1(i64 %172) #8
  unreachable

183:                                              ; preds = %178, %for.end
  store i8 0, i8* %arrayidx21, align 16
  %184 = bitcast i32* %i22 to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %184) #3
  store i32 0, i32* %i22, align 4
  br label %for.cond23

for.cond23:                                       ; preds = %for.inc33, %183
  %185 = load i32, i32* %i22, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 8, i32 %185)
  %cmp24 = icmp slt i32 %185, 8
  br i1 %cmp24, label %for.body26, label %for.cond.cleanup25

for.cond.cleanup25:                               ; preds = %for.cond23
  store i32 8, i32* %cleanup.dest.slot, align 4
  %186 = bitcast i32* %i22 to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %186) #3
  br label %for.end35

for.body26:                                       ; preds = %for.cond23
  %187 = load i32, i32* %i22, align 4
  %add27 = add nsw i32 %187, 44
  %add28 = add nsw i32 %add27, 16
  %idxprom29 = sext i32 %add28 to i64
  %arrayidx30 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 %idxprom29
  %188 = ptrtoint i8* %arrayidx30 to i64
  %189 = lshr i64 %188, 3
  %190 = add i64 %189, 2147450880
  %191 = inttoptr i64 %190 to i8*
  %192 = load i8, i8* %191, align 1
  %193 = icmp ne i8 %192, 0
  br i1 %193, label %194, label %199, !prof !31

194:                                              ; preds = %for.body26
  %195 = and i64 %188, 7
  %196 = trunc i64 %195 to i8
  %197 = icmp sge i8 %196, %192
  br i1 %197, label %198, label %199

198:                                              ; preds = %194
  call void @__asan_report_load1(i64 %188) #8
  unreachable

199:                                              ; preds = %194, %for.body26
  %200 = load i8, i8* %arrayidx30, align 1
  %201 = load i32, i32* %i22, align 4
  %idxprom31 = sext i32 %201 to i64
  %arrayidx32 = getelementptr inbounds [201 x i8], [201 x i8]* %20, i64 0, i64 %idxprom31
  %202 = ptrtoint i8* %arrayidx32 to i64
  %203 = lshr i64 %202, 3
  %204 = add i64 %203, 2147450880
  %205 = inttoptr i64 %204 to i8*
  %206 = load i8, i8* %205, align 1
  %207 = icmp ne i8 %206, 0
  br i1 %207, label %208, label %213, !prof !31

208:                                              ; preds = %199
  %209 = and i64 %202, 7
  %210 = trunc i64 %209 to i8
  %211 = icmp sge i8 %210, %206
  br i1 %211, label %212, label %213

212:                                              ; preds = %208
  call void @__asan_report_store1(i64 %202) #8
  unreachable

213:                                              ; preds = %208, %199
  store i8 %200, i8* %arrayidx32, align 1
  br label %for.inc33

for.inc33:                                        ; preds = %213
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 28) to i32*)) #8
  %214 = load i32, i32* %i22, align 4
  %inc34 = add nsw i32 %214, 1
  store i32 %inc34, i32* %i22, align 4
  br label %for.cond23, !llvm.loop !33

for.end35:                                        ; preds = %for.cond.cleanup25
  %arrayidx36 = getelementptr inbounds [201 x i8], [201 x i8]* %20, i64 0, i64 8
  %215 = ptrtoint i8* %arrayidx36 to i64
  %216 = lshr i64 %215, 3
  %217 = add i64 %216, 2147450880
  %218 = inttoptr i64 %217 to i8*
  %219 = load i8, i8* %218, align 1
  %220 = icmp ne i8 %219, 0
  br i1 %220, label %221, label %226, !prof !31

221:                                              ; preds = %for.end35
  %222 = and i64 %215, 7
  %223 = trunc i64 %222 to i8
  %224 = icmp sge i8 %223, %219
  br i1 %224, label %225, label %226

225:                                              ; preds = %221
  call void @__asan_report_store1(i64 %215) #8
  unreachable

226:                                              ; preds = %221, %for.end35
  store i8 0, i8* %arrayidx36, align 8
  %227 = bitcast i32* %i37 to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %227) #3
  store i32 0, i32* %i37, align 4
  br label %for.cond38

for.cond38:                                       ; preds = %for.inc49, %226
  %228 = load i32, i32* %i37, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 4, i32 %228)
  %cmp39 = icmp slt i32 %228, 4
  br i1 %cmp39, label %for.body41, label %for.cond.cleanup40

for.cond.cleanup40:                               ; preds = %for.cond38
  store i32 11, i32* %cleanup.dest.slot, align 4
  %229 = bitcast i32* %i37 to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %229) #3
  br label %for.end51

for.body41:                                       ; preds = %for.cond38
  %230 = load i32, i32* %i37, align 4
  %add42 = add nsw i32 %230, 44
  %add43 = add nsw i32 %add42, 16
  %add44 = add nsw i32 %add43, 8
  %idxprom45 = sext i32 %add44 to i64
  %arrayidx46 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 %idxprom45
  %231 = ptrtoint i8* %arrayidx46 to i64
  %232 = lshr i64 %231, 3
  %233 = add i64 %232, 2147450880
  %234 = inttoptr i64 %233 to i8*
  %235 = load i8, i8* %234, align 1
  %236 = icmp ne i8 %235, 0
  br i1 %236, label %237, label %242, !prof !31

237:                                              ; preds = %for.body41
  %238 = and i64 %231, 7
  %239 = trunc i64 %238 to i8
  %240 = icmp sge i8 %239, %235
  br i1 %240, label %241, label %242

241:                                              ; preds = %237
  call void @__asan_report_load1(i64 %231) #8
  unreachable

242:                                              ; preds = %237, %for.body41
  %243 = load i8, i8* %arrayidx46, align 1
  %244 = load i32, i32* %i37, align 4
  %idxprom47 = sext i32 %244 to i64
  %arrayidx48 = getelementptr inbounds [201 x i8], [201 x i8]* %22, i64 0, i64 %idxprom47
  %245 = ptrtoint i8* %arrayidx48 to i64
  %246 = lshr i64 %245, 3
  %247 = add i64 %246, 2147450880
  %248 = inttoptr i64 %247 to i8*
  %249 = load i8, i8* %248, align 1
  %250 = icmp ne i8 %249, 0
  br i1 %250, label %251, label %256, !prof !31

251:                                              ; preds = %242
  %252 = and i64 %245, 7
  %253 = trunc i64 %252 to i8
  %254 = icmp sge i8 %253, %249
  br i1 %254, label %255, label %256

255:                                              ; preds = %251
  call void @__asan_report_store1(i64 %245) #8
  unreachable

256:                                              ; preds = %251, %242
  store i8 %243, i8* %arrayidx48, align 1
  br label %for.inc49

for.inc49:                                        ; preds = %256
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 32) to i32*)) #8
  %257 = load i32, i32* %i37, align 4
  %inc50 = add nsw i32 %257, 1
  store i32 %inc50, i32* %i37, align 4
  br label %for.cond38, !llvm.loop !34

for.end51:                                        ; preds = %for.cond.cleanup40
  %arrayidx52 = getelementptr inbounds [201 x i8], [201 x i8]* %22, i64 0, i64 4
  %258 = ptrtoint i8* %arrayidx52 to i64
  %259 = lshr i64 %258, 3
  %260 = add i64 %259, 2147450880
  %261 = inttoptr i64 %260 to i8*
  %262 = load i8, i8* %261, align 1
  %263 = icmp ne i8 %262, 0
  br i1 %263, label %264, label %269, !prof !31

264:                                              ; preds = %for.end51
  %265 = and i64 %258, 7
  %266 = trunc i64 %265 to i8
  %267 = icmp sge i8 %266, %262
  br i1 %267, label %268, label %269

268:                                              ; preds = %264
  call void @__asan_report_store1(i64 %258) #8
  unreachable

269:                                              ; preds = %264, %for.end51
  store i8 0, i8* %arrayidx52, align 4
  %arraydecay53 = getelementptr inbounds [201 x i8], [201 x i8]* %22, i64 0, i64 0
  %call54 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.8, i32 0, i32 0, i64 0), i8* %arraydecay53)
  %270 = bitcast i64* %x to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %270) #3
  %arraydecay55 = getelementptr inbounds [201 x i8], [201 x i8]* %18, i64 0, i64 0
  %call56 = call i64 @strtoull(i8* %arraydecay55, i8** null, i32 16) #3
  store i64 %call56, i64* %x, align 8
  %271 = load i64, i64* %x, align 8
  call void @__sanitizer_cov_trace_const_cmp8(i64 -3819410105351357762, i64 %271)
  %cmp57 = icmp ne i64 %271, -3819410105351357762
  br i1 %cmp57, label %if.then58, label %if.end59

if.then58:                                        ; preds = %269
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 36) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup76

if.end59:                                         ; preds = %269
  %272 = bitcast i32* %y to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %272) #3
  %arraydecay60 = getelementptr inbounds [201 x i8], [201 x i8]* %20, i64 0, i64 0
  %call61 = call i64 @strtoul(i8* %arraydecay60, i8** null, i32 16) #3
  %conv = trunc i64 %call61 to i32
  store i32 %conv, i32* %y, align 4
  %273 = load i32, i32* %y, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 -559038242, i32 %273)
  %cmp62 = icmp ne i32 %273, -559038242
  br i1 %cmp62, label %if.then63, label %if.end64

if.then63:                                        ; preds = %if.end59
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 40) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup75

if.end64:                                         ; preds = %if.end59
  %274 = bitcast i16* %z to i8*
  call void @llvm.lifetime.start.p0i8(i64 2, i8* %274) #3
  %arraydecay65 = getelementptr inbounds [201 x i8], [201 x i8]* %22, i64 0, i64 0
  %call66 = call i64 @strtouq(i8* %arraydecay65, i8** null, i32 16) #3
  %conv67 = trunc i64 %call66 to i16
  store i16 %conv67, i16* %z, align 2
  %275 = load i16, i16* %z, align 2
  %conv68 = zext i16 %275 to i32
  %276 = zext i32 %conv68 to i64
  call void @__sanitizer_cov_trace_switch(i64 %276, i64* getelementptr inbounds ([5 x i64], [5 x i64]* @__sancov_gen_cov_switch_values.11, i32 0, i32 0))
  switch i32 %conv68, label %sw.default72 [
    i32 48879, label %sw.bb69
    i32 65259, label %sw.bb70
    i32 61374, label %sw.bb71
  ]

sw.bb69:                                          ; preds = %if.end64
  br label %sw.epilog73

sw.bb70:                                          ; preds = %if.end64
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 44) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.bb71:                                          ; preds = %if.end64
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 48) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.default72:                                     ; preds = %if.end64
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 52) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.epilog73:                                      ; preds = %sw.bb69
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 56) to i32*)) #8
  %call74 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.9, i32 0, i32 0, i64 0))
  store i32 0, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

cleanup:                                          ; preds = %sw.epilog73, %sw.default72, %sw.bb71, %sw.bb70
  %277 = bitcast i16* %z to i8*
  call void @llvm.lifetime.end.p0i8(i64 2, i8* %277) #3
  br label %cleanup75

cleanup75:                                        ; preds = %cleanup, %if.then63
  %278 = bitcast i32* %y to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %278) #3
  br label %cleanup76

cleanup76:                                        ; preds = %cleanup75, %if.then58
  %279 = bitcast i64* %x to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %279) #3
  %280 = bitcast [201 x i8]* %22 to i8*
  %281 = add i64 %29, 118
  %282 = inttoptr i64 %281 to i64*
  store i64 -506381209866536712, i64* %282, align 1
  %283 = add i64 %29, 126
  %284 = inttoptr i64 %283 to i64*
  store i64 -506381209866536712, i64* %284, align 1
  %285 = add i64 %29, 134
  %286 = inttoptr i64 %285 to i64*
  store i64 -506381209866536712, i64* %286, align 1
  %287 = add i64 %29, 142
  %288 = inttoptr i64 %287 to i16*
  store i16 -1800, i16* %288, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %280) #3
  %289 = bitcast [201 x i8]* %20 to i8*
  %290 = add i64 %29, 84
  %291 = inttoptr i64 %290 to i64*
  store i64 -506381209866536712, i64* %291, align 1
  %292 = add i64 %29, 92
  %293 = inttoptr i64 %292 to i64*
  store i64 -506381209866536712, i64* %293, align 1
  %294 = add i64 %29, 100
  %295 = inttoptr i64 %294 to i64*
  store i64 -506381209866536712, i64* %295, align 1
  %296 = add i64 %29, 108
  %297 = inttoptr i64 %296 to i16*
  store i16 -1800, i16* %297, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %289) #3
  %298 = bitcast [201 x i8]* %18 to i8*
  %299 = add i64 %29, 50
  %300 = inttoptr i64 %299 to i64*
  store i64 -506381209866536712, i64* %300, align 1
  %301 = add i64 %29, 58
  %302 = inttoptr i64 %301 to i64*
  store i64 -506381209866536712, i64* %302, align 1
  %303 = add i64 %29, 66
  %304 = inttoptr i64 %303 to i64*
  store i64 -506381209866536712, i64* %304, align 1
  %305 = add i64 %29, 74
  %306 = inttoptr i64 %305 to i16*
  store i16 -1800, i16* %306, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %298) #3
  br label %cleanup80

cleanup80:                                        ; preds = %cleanup76, %if.then
  %307 = bitcast [45 x i8]* %16 to i8*
  %308 = add i64 %29, 40
  %309 = inttoptr i64 %308 to i32*
  store i32 -117901064, i32* %309, align 1
  %310 = add i64 %29, 44
  %311 = inttoptr i64 %310 to i16*
  store i16 -1800, i16* %311, align 1
  call void @llvm.lifetime.end.p0i8(i64 45, i8* %307) #3
  %312 = bitcast %struct._IO_FILE** %fp to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %312) #3
  %313 = bitcast [201 x i8]* %14 to i8*
  %314 = add i64 %29, 6
  %315 = inttoptr i64 %314 to i64*
  store i64 -506381209866536712, i64* %315, align 1
  %316 = add i64 %29, 14
  %317 = inttoptr i64 %316 to i64*
  store i64 -506381209866536712, i64* %317, align 1
  %318 = add i64 %29, 22
  %319 = inttoptr i64 %318 to i64*
  store i64 -506381209866536712, i64* %319, align 1
  %320 = add i64 %29, 30
  %321 = inttoptr i64 %320 to i16*
  store i16 -1800, i16* %321, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %313) #3
  %322 = bitcast i8** %filename to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %322) #3
  %323 = bitcast i32* %12 to i8*
  %324 = add i64 %29, 4
  %325 = inttoptr i64 %324 to i8*
  store i8 -8, i8* %325, align 1
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %323) #3
  %326 = bitcast i32* %opt to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %326) #3
  %327 = load i32, i32* %retval, align 4
  store i64 1172321806, i64* %23, align 8
  %328 = icmp ne i64 %5, 0
  br i1 %328, label %329, label %330

329:                                              ; preds = %cleanup80
  call void @__asan_stack_free_5(i64 %5, i64 1216)
  br label %332

330:                                              ; preds = %cleanup80
  %331 = add i64 %29, 0
  call void @__asan_set_shadow_00(i64 %331, i64 152)
  br label %332

332:                                              ; preds = %330, %329
  ret i32 %327
}

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.start.p0i8(i64 immarg, i8* nocapture) #5

; Function Attrs: nounwind
declare dso_local i32 @getopt_long(i32, i8**, i8*, %struct.option*, i32*) #2

declare dso_local i32 @printf(i8*, ...) #1

declare dso_local %struct._IO_FILE* @fopen(i8*, i8*) #1

declare dso_local i8* @fgets(i8*, i32, %struct._IO_FILE*) #1

; Function Attrs: argmemonly nofree nosync nounwind willreturn writeonly
declare void @llvm.memset.p0i8.i64(i8* nocapture writeonly, i8, i64, i1 immarg) #6

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg) #5

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @memcmp(i8*, i8*, i64) #7

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @strncmp(i8*, i8*, i64) #7

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @strcmp(i8*, i8*) #7

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.end.p0i8(i64 immarg, i8* nocapture) #5

; Function Attrs: nounwind
declare dso_local i64 @strtoull(i8*, i8**, i32) #2

; Function Attrs: nounwind
declare dso_local i64 @strtoul(i8*, i8**, i32) #2

; Function Attrs: nounwind
declare dso_local i64 @strtouq(i8*, i8**, i32) #2

; Function Attrs: noinline sanitize_address uwtable
define internal void @_GLOBAL__sub_I_demo.cc() #0 section ".text.startup" comdat($"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f") {
entry:
  call void @__asan_before_dynamic_init(i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64))
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([1 x i32], [1 x i32]* @__sancov_gen_.12, i32 0, i32 0)) #8
  call void @__cxx_global_var_init()
  call void @__asan_after_dynamic_init()
  ret void
}

declare void @__sanitizer_cov_trace_pc_indir(i64)

declare void @__sanitizer_cov_trace_cmp1(i8 zeroext, i8 zeroext)

declare void @__sanitizer_cov_trace_cmp2(i16 zeroext, i16 zeroext)

declare void @__sanitizer_cov_trace_cmp4(i32 zeroext, i32 zeroext)

declare void @__sanitizer_cov_trace_cmp8(i64, i64)

declare void @__sanitizer_cov_trace_const_cmp1(i8 zeroext, i8 zeroext)

declare void @__sanitizer_cov_trace_const_cmp2(i16 zeroext, i16 zeroext)

declare void @__sanitizer_cov_trace_const_cmp4(i32 zeroext, i32 zeroext)

declare void @__sanitizer_cov_trace_const_cmp8(i64, i64)

declare void @__sanitizer_cov_trace_div4(i32 zeroext)

declare void @__sanitizer_cov_trace_div8(i64)

declare void @__sanitizer_cov_trace_gep(i64)

declare void @__sanitizer_cov_trace_switch(i64, i64*)

declare void @__sanitizer_cov_trace_pc()

declare void @__sanitizer_cov_trace_pc_guard(i32*)

declare void @__sanitizer_cov_trace_pc_guard_init(i32*, i32*)

define internal void @sancov.module_ctor_trace_pc_guard() comdat {
  call void @__asan_before_dynamic_init(i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64))
  call void @__sanitizer_cov_trace_pc_guard_init(i32* @__start___sancov_guards, i32* @__stop___sancov_guards)
  call void @__asan_after_dynamic_init()
  ret void
}

declare void @__asan_report_load_n(i64, i64)

declare void @__asan_loadN(i64, i64)

declare void @__asan_report_load1(i64)

declare void @__asan_load1(i64)

declare void @__asan_report_load2(i64)

declare void @__asan_load2(i64)

declare void @__asan_report_load4(i64)

declare void @__asan_load4(i64)

declare void @__asan_report_load8(i64)

declare void @__asan_load8(i64)

declare void @__asan_report_load16(i64)

declare void @__asan_load16(i64)

declare void @__asan_report_store_n(i64, i64)

declare void @__asan_storeN(i64, i64)

declare void @__asan_report_store1(i64)

declare void @__asan_store1(i64)

declare void @__asan_report_store2(i64)

declare void @__asan_store2(i64)

declare void @__asan_report_store4(i64)

declare void @__asan_store4(i64)

declare void @__asan_report_store8(i64)

declare void @__asan_store8(i64)

declare void @__asan_report_store16(i64)

declare void @__asan_store16(i64)

declare void @__asan_report_exp_load_n(i64, i64, i32)

declare void @__asan_exp_loadN(i64, i64, i32)

declare void @__asan_report_exp_load1(i64, i32)

declare void @__asan_exp_load1(i64, i32)

declare void @__asan_report_exp_load2(i64, i32)

declare void @__asan_exp_load2(i64, i32)

declare void @__asan_report_exp_load4(i64, i32)

declare void @__asan_exp_load4(i64, i32)

declare void @__asan_report_exp_load8(i64, i32)

declare void @__asan_exp_load8(i64, i32)

declare void @__asan_report_exp_load16(i64, i32)

declare void @__asan_exp_load16(i64, i32)

declare void @__asan_report_exp_store_n(i64, i64, i32)

declare void @__asan_exp_storeN(i64, i64, i32)

declare void @__asan_report_exp_store1(i64, i32)

declare void @__asan_exp_store1(i64, i32)

declare void @__asan_report_exp_store2(i64, i32)

declare void @__asan_exp_store2(i64, i32)

declare void @__asan_report_exp_store4(i64, i32)

declare void @__asan_exp_store4(i64, i32)

declare void @__asan_report_exp_store8(i64, i32)

declare void @__asan_exp_store8(i64, i32)

declare void @__asan_report_exp_store16(i64, i32)

declare void @__asan_exp_store16(i64, i32)

declare i8* @__asan_memmove(i8*, i8*, i64)

declare i8* @__asan_memcpy(i8*, i8*, i64)

declare i8* @__asan_memset(i8*, i32, i64)

declare void @__asan_handle_no_return()

declare void @__sanitizer_ptr_cmp(i64, i64)

declare void @__sanitizer_ptr_sub(i64, i64)

declare i64 @__asan_stack_malloc_0(i64)

declare void @__asan_stack_free_0(i64, i64)

declare i64 @__asan_stack_malloc_1(i64)

declare void @__asan_stack_free_1(i64, i64)

declare i64 @__asan_stack_malloc_2(i64)

declare void @__asan_stack_free_2(i64, i64)

declare i64 @__asan_stack_malloc_3(i64)

declare void @__asan_stack_free_3(i64, i64)

declare i64 @__asan_stack_malloc_4(i64)

declare void @__asan_stack_free_4(i64, i64)

declare i64 @__asan_stack_malloc_5(i64)

declare void @__asan_stack_free_5(i64, i64)

declare i64 @__asan_stack_malloc_6(i64)

declare void @__asan_stack_free_6(i64, i64)

declare i64 @__asan_stack_malloc_7(i64)

declare void @__asan_stack_free_7(i64, i64)

declare i64 @__asan_stack_malloc_8(i64)

declare void @__asan_stack_free_8(i64, i64)

declare i64 @__asan_stack_malloc_9(i64)

declare void @__asan_stack_free_9(i64, i64)

declare i64 @__asan_stack_malloc_10(i64)

declare void @__asan_stack_free_10(i64, i64)

declare void @__asan_poison_stack_memory(i64, i64)

declare void @__asan_unpoison_stack_memory(i64, i64)

declare void @__asan_set_shadow_00(i64, i64)

declare void @__asan_set_shadow_f1(i64, i64)

declare void @__asan_set_shadow_f2(i64, i64)

declare void @__asan_set_shadow_f3(i64, i64)

declare void @__asan_set_shadow_f5(i64, i64)

declare void @__asan_set_shadow_f8(i64, i64)

declare void @__asan_alloca_poison(i64, i64)

declare void @__asan_allocas_unpoison(i64, i64)

declare void @__asan_before_dynamic_init(i64)

declare void @__asan_after_dynamic_init()

declare void @__asan_register_globals(i64, i64)

declare void @__asan_unregister_globals(i64, i64)

declare void @__asan_register_image_globals(i64)

declare void @__asan_unregister_image_globals(i64)

declare void @__asan_register_elf_globals(i64, i64, i64)

declare void @__asan_unregister_elf_globals(i64, i64, i64)

declare void @__asan_init()

define internal void @asan.module_ctor() {
  call void @__asan_init()
  call void @__asan_version_mismatch_check_v8()
  call void @__asan_register_globals(i64 ptrtoint ([12 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 12)
  ret void
}

declare void @__asan_version_mismatch_check_v8()

define internal void @asan.module_dtor() {
  call void @__asan_unregister_globals(i64 ptrtoint ([12 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 12)
  ret void
}

attributes #0 = { noinline sanitize_address uwtable "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }
attributes #4 = { noinline norecurse optnone sanitize_address uwtable mustprogress "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #5 = { argmemonly nofree nosync nounwind willreturn }
attributes #6 = { argmemonly nofree nosync nounwind willreturn writeonly }
attributes #7 = { nounwind readonly willreturn "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #8 = { nomerge }
attributes #9 = { nobuiltin nounwind readonly willreturn }
attributes #10 = { nounwind readonly willreturn }

!llvm.asan.globals = !{!3, !5, !7, !9, !11, !13, !15, !17, !19, !21, !23, !25}
!llvm.module.flags = !{!27}
!llvm.ident = !{!28}

!0 = !{void ()* @__cxx_global_var_init}
!1 = !{i32 (i32, i8**)* @main}
!2 = !{void ()* @_GLOBAL__sub_I_demo.cc}
!3 = !{%"class.std::ios_base::Init"* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0), !4, !"std::__ioinit", i1 true, i1 false}
!4 = !{!"/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream", i32 74, i32 25}
!5 = !{[5 x i8]* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0), !6, !"<string literal>", i1 false, i1 false}
!6 = !{!"demo/demo.cc", i32 20, i32 10}
!7 = !{[1 x %struct.option]* getelementptr inbounds ({ [1 x %struct.option], [32 x i8] }, { [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options, i32 0, i32 0), !8, !"long_options", i1 false, i1 false}
!8 = !{!"demo/demo.cc", i32 18, i32 26}
!9 = !{[3 x i8]* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0), !10, !"<string literal>", i1 false, i1 false}
!10 = !{!"demo/demo.cc", i32 22, i32 42}
!11 = !{[18 x i8]* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0), !12, !"<string literal>", i1 false, i1 false}
!12 = !{!"demo/demo.cc", i32 31, i32 20}
!13 = !{[2 x i8]* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0), !14, !"<string literal>", i1 false, i1 false}
!14 = !{!"demo/demo.cc", i32 39, i32 32}
!15 = !{[21 x i8]* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.4, i32 0, i32 0), !16, !"<string literal>", i1 false, i1 false}
!16 = !{!"demo/demo.cc", i32 52, i32 28}
!17 = !{[12 x i8]* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.5, i32 0, i32 0), !18, !"<string literal>", i1 false, i1 false}
!18 = !{!"demo/demo.cc", i32 53, i32 30}
!19 = !{[14 x i8]* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.6, i32 0, i32 0), !20, !"<string literal>", i1 false, i1 false}
!20 = !{!"demo/demo.cc", i32 54, i32 29}
!21 = !{[27 x i8]* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.7, i32 0, i32 0), !22, !"<string literal>", i1 false, i1 false}
!22 = !{!"demo/demo.cc", i32 58, i32 12}
!23 = !{[4 x i8]* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.8, i32 0, i32 0), !24, !"<string literal>", i1 false, i1 false}
!24 = !{!"demo/demo.cc", i32 73, i32 12}
!25 = !{[33 x i8]* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.9, i32 0, i32 0), !26, !"<string literal>", i1 false, i1 false}
!26 = !{!"demo/demo.cc", i32 101, i32 12}
!27 = !{i32 1, !"wchar_size", i32 4}
!28 = !{!"clang version 12.0.1 (git@github.com:fengzhengzhan/BTFuzz.git 0b64f5806b4302732328fa068687800669443ef8)"}
!29 = distinct !{!29, !30}
!30 = !{!"llvm.loop.mustprogress"}
!31 = !{!"branch_weights", i32 1, i32 100000}
!32 = distinct !{!32, !30}
!33 = distinct !{!33, !30}
!34 = distinct !{!34, !30}

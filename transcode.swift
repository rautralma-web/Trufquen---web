import AVFoundation
import Foundation
let a = CommandLine.arguments
let src = URL(fileURLWithPath: a[1]); let dst = URL(fileURLWithPath: a[2])
let start = Double(a[3])!; let dur = Double(a[4])!
let outW = Int(a[5])!; let bitrate = Int(a[6])!
let asset = AVURLAsset(url: src)
guard let track = asset.tracks(withMediaType: .video).first else { print("sin video"); exit(2) }
let nat = track.naturalSize.applying(track.preferredTransform)
let srcW = abs(nat.width), srcH = abs(nat.height)
let outH = Int((CGFloat(outW) * srcH / srcW / 2).rounded() * 2)
try? FileManager.default.removeItem(at: dst)
let reader = try! AVAssetReader(asset: asset)
reader.timeRange = CMTimeRange(start: CMTime(seconds: start, preferredTimescale: 600), duration: CMTime(seconds: dur, preferredTimescale: 600))
let rOut = AVAssetReaderTrackOutput(track: track, outputSettings: [kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange])
reader.add(rOut)
let writer = try! AVAssetWriter(outputURL: dst, fileType: .mp4)
writer.shouldOptimizeForNetworkUse = true
let wIn = AVAssetWriterInput(mediaType: .video, outputSettings: [AVVideoCodecKey: AVVideoCodecType.h264, AVVideoWidthKey: outW, AVVideoHeightKey: outH, AVVideoCompressionPropertiesKey: [AVVideoAverageBitRateKey: bitrate, AVVideoProfileLevelKey: AVVideoProfileLevelH264HighAutoLevel, AVVideoMaxKeyFrameIntervalKey: 60]])
wIn.expectsMediaDataInRealTime = false
writer.add(wIn)
writer.startWriting(); reader.startReading(); writer.startSession(atSourceTime: reader.timeRange.start)
let q = DispatchQueue(label: "t"); let sem = DispatchSemaphore(value: 0)
wIn.requestMediaDataWhenReady(on: q) { while wIn.isReadyForMoreMediaData { if let sb = rOut.copyNextSampleBuffer() { wIn.append(sb) } else { wIn.markAsFinished(); writer.finishWriting { sem.signal() }; break } } }
sem.wait()
let kb = ((try? FileManager.default.attributesOfItem(atPath: dst.path)[.size] as? Int ?? 0) ?? 0) / 1024
print("OK \(dst.lastPathComponent) \(outW)x\(outH) \(kb) KB")
